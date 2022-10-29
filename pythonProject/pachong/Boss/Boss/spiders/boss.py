import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.zhipin.com/web/geek/job?query=c%2B%2B&city=101110100']

    def parse(self, response):
        #print(response.text)
        print(response)
        li_list = response.xpath('//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li')
        print(li_list)

