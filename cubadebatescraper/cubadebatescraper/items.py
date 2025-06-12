# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CubadebatescraperItem(scrapy.Item):
    # define the fields for your item here like:
    title      = scrapy.Field()
    url        = scrapy.Field()
    tags       = scrapy.Field()
    image_text = scrapy.Field()
    shore_text = scrapy.Field()
