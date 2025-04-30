import scrapy
from web_crawler_demo.items import item1 
from scrapy.exceptions import CloseSpider

class Spider2(scrapy.Spider):
    name = "spider2"
    start_urls = ['http://quotes.toscrape.com']

    def __init__(self, should_scrape='n', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.should_scrape = should_scrape.lower()

    def parse(self, response):
        if self.should_scrape == 'y':
            quotes = response.xpath('//div[@class="quote"]')
            if not quotes:
                raise CloseSpider('No quotes found on the page.')
            for quote in quotes:
                item = item1()
                item['title'] = quote.xpath('.//span[@class="text"]/text()').get()
                item['link'] = response.url
                yield item

#  scrapy crawl spider2 -a should_scrape=y for the spider to run

