# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def __init__(self, category=None, *args, **kwargs):
        super(BaiduSpider, self).__init__(*args, **kwargs)
        self.category = category

    # def start_requests(self):
    #     yield scrapy.Request(url='http://www.baidu.com/', callback=self.parse_index)

    def make_requests_from_url(self, url):
        print("yes")
        return scrapy.Request(url=url, callback= self.parse_index)

    def parse(self, response):
        pass

    def parse_index(self, response):
        # print('baidu%s'%response.status)
        self.logger.critical(self.category)