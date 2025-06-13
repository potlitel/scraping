# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import psycopg2

class CubadebatescraperPipeline:
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline:

    def __init__(self):
        self.names_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['title'] in self.names_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.names_seen.add(adapter['title'])
            return item       

class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()
        # https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-postgres/ (include: Only Saving New Data)
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS catalogs.public.cubadebate_news (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            url TEXT,
            tags VARCHAR(255),
            image_text VARCHAR(255),
            shore_text TEXT
            );
        """)


    def create_connection(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="catalogs",
            user="citizix_user",
            password="S3cret")

        self.curr = self.connection.cursor()


    def process_item(self, item, spider):
        self.store_db(item)
        #we need to return the item below as scrapy expects us to!
        return item

    def store_db(self, item):
        try:
            self.curr.execute(""" insert into cubadebate_news (title, url, tags, image_text, shore_text) values (%s, %s, %s, %s, %s)""", 
            (
                item["title"],
                item["url"],
                item["tags"],
                item["image_text"],
                item["shore_text"]
            ))

        except BaseException as e:
            print(e)
            self.connection.commit()
 
