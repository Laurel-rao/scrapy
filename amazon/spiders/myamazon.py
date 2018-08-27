# -*- coding: utf-8 -*-
import random

import time

import scrapy
from urllib import parse
from ..items import AmazonItem
from ..user_agent import user_agent

class MyamazonSpider(scrapy.Spider):

    name = 'myamazon'
    allowed_domains = ['https://www.amazon.cn/']
    ua = user_agent().get_ua()
    custom_settings = {'DEFAULT_REQUEST_HEADERS': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'User-Agent':ua
    }}

    keyword = 'iphonex'
    base_url = 'https://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&'
    start_urls = [base_url + parse.urlencode({'field-keywords':keyword})]

    def parse(self, response):
        url_list = response.css('.pagnDisabled::text').extract_first()
        print(url_list)
        for i in range(1, int(url_list)+1):
            info_url = response.url+'&'+parse.urlencode({'page':i})

            yield scrapy.Request(info_url, callback = self.info_parse, dont_filter=True)

    def info_parse(self, response):

        ite = response.css('#s-results-list-atf>li')
        for i in ite:
            time.sleep(random.uniform(1,3))
            title = i.css('h2::text').extract_first()
            url = i.css('a.a-link-normal::attr(href)').extract_first()
            price = i.css('span.a-color-price::text').extract_first()
            score = i.css('span.a-icon span.a-icon-alt::text').extract_first()
            item = AmazonItem()
            item['title'] = title
            item['url'] = url
            item['price'] = price
            item['score'] = score
            yield item












