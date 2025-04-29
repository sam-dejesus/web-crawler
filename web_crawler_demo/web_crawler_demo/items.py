
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class item1(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    pass
