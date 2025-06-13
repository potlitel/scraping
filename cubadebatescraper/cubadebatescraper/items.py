# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CubadebatescraperItem(scrapy.Item):
    # Field() acts as a placeholder for whatever we're going to put inside the scrapy.Item.
    # This allows us to pass in anything for custom processing or add default values.
    # define the fields for your item here like:
    title      = scrapy.Field()
    url        = scrapy.Field()
    tags       = scrapy.Field()
    image_text = scrapy.Field()
    shore_text = scrapy.Field()
