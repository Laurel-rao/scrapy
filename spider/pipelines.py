# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

import pymongo
from scrapy.exceptions import DropItem


class TencentspiderPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        '''
        保存到json文件
        :param item:
        :param spider:
        :return:
        '''
        # file = os.getcwd() + '\\' + 'shuju.txt'
        # print(file)
        # with open(file, 'ab') as ff:
        #     text = json.dumps(dict(item), ensure_ascii=False) + '\n'

        # 数据清洗
        if None:
            # 数据为空，或异常
            raise DropItem('xxx')

        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


# 写入数据库
class MongoPipeline(object):
    def __init__(self, mongo_uri=None, mongo_db=None, collection_name=None):
        if mongo_uri and mongo_db and collection_name:
            self.mongo_uri = mongo_uri
            self.mongo_db = mongo_db
            self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        #  获取settings 的配置

        mongo_uri = crawler.settings.get("MONGO_URI")
        mongo_db = crawler.settings.get('MONGO_DB')
        collection_name = crawler.settings.get('MONGO_COLLECTION')

        return cls(mongo_uri, mongo_db, collection_name)

    def open_spider(self, spider):
        # 连接数据库
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 执行对数据库的操作
        print(item)
        self.db[self.collection_name].insert(dict(item))
        return item

