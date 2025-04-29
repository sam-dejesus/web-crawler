import scrapy
from web_crawler_demo.items import item1


class Spider1Spider(scrapy.Spider):
    name = "spider1"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        item = item1()
        item['title'] = response.xpath('//span[@class="text"]/text()').get()
        item['link'] = response.url
        yield item
        pass
