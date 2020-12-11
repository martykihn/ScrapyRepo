# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyplotsItem(scrapy.Item):
   url = scrapy.Field()
   title = scrapy.Field()
   spoiler = scrapy.Field()
