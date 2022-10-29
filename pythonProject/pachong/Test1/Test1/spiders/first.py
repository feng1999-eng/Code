import scrapy
import re
from icecream import ic
from Test1.items import Test1Item

class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://h5.17k.com/']

    def parse(self, response):
        a_list = response.xpath('//dl[@id="Jingpin_box"]/dd/a')
        all_data = []
        for a in a_list:
            name_span = a.xpath('./span[1]')[0].extract()
            author_span = a.xpath('./span[2]')[0].extract()
            name = re.findall(r'<span class="name">(.*?)</span>', name_span)[0]
            author = re.findall(r'<span class="author">(.*?)</span>', author_span)[0]
        #     dic = {
        #         "name": name,
        #         "author": author
        #     }
        #     all_data.append(dic)
        # return all_data
            item = Test1Item()
            item["name"]= name
            item["author"] = author
            yield item

