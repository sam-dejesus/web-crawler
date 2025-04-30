import scrapy
from web_crawler_demo.items import *
class Spider4(scrapy.Spider):
    name = "spider4"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):

        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = item1()
            item['title'] = quote.xpath('.//span[@class="text"]/text()').get()
            item['link'] = response.url
            item['tags'] = quote.xpath('.//a[@class="tag"]/text()').getall()
            yield item

        next_page = response.css('li.next a::attr(href)').get() 
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, self.parse)