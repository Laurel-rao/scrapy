# -*- coding: utf-8 -*-
import scrapy
from ..items import *


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = []
    # 对 请求头 进行设置
    custom_settings = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
    }
    for i in range(0,511,10):
        start_urls.append('https://hr.tencent.com/position.php?keywords=python&start=%d#a'%i)

    def parse(self, response):

        i = response.css('.tablelist>tr:not(.h)')
        # <class 'scrapy.selector.unified.SelectorList'>
        descriptions = i.css('td>a::text').extract()
        urls = i.css('td>a::attr(href)').extract()
        locations = i.css('td:nth-child(4)::text').extract()
        release_times = i.css('td:nth-child(5)::text').extract()
        item = TencentspiderItem()
        for description, url, location, release_time in zip(descriptions, urls, locations, release_times):
            item['description'] = description
            item['url'] = url
            item['location'] = location
            item['release_time'] = release_time
            # print(item)
            yield item