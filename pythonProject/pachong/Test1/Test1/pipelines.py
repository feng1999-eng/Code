# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Test1Pipeline:
    def open_spider(self, spider):
        fp = None
        print("开始爬虫...")
        self.fp = open('./xiaoshuo.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        name = item["name"]
        author = item["author"]
        self.fp.write(name+":"+author+'\n')
        return item
    def close_spider(self, spider):
        print("关闭爬虫！")
        self.fp.close()