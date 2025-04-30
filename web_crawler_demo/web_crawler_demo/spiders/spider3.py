import scrapy
from web_crawler_demo.items import *
from scrapy.exceptions import CloseSpider
class Spider3(scrapy.Spider):
    name = "spider3"
    start_urls = ['http://quotes.toscrape.com']

    def __init__(self, cats='a', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cats = cats.lower()

    def parse(self, response):
        if self.cats == 'a':
            quotes = response.xpath('//div[@class="quote"]')
            for quote in quotes:
                item = item1()
                item['title'] = quote.xpath('.//span[@class="text"]/text()').get()
                item['link'] = response.url
                item['tags'] = quote.xpath('.//a[@class="tag"]/text()').getall()
                yield item
        elif self.cats == 'b':
            quotes = response.xpath('//div[@class="quote"]')
            for quote in quotes:
                item = item2()
                item['title'] = quote.xpath('.//span[@class="text"]/text()').get()
                item['link'] = response.url
                yield item
        elif self.cats == 'c':
            quotes = response.xpath('//div[@class="quote"]')
            for quote in quotes:
                item = item3()
                item['title'] = quote.xpath('.//span[@class="text"]/text()').get()
                yield item
        else:
            raise CloseSpider('Param Error check input values')
