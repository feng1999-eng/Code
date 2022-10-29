import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
