# -*- coding: utf-8 -*-
import scrapy


class UsSpider(scrapy.Spider):
    name = 'us'
    allowed_domains = ['163.com']
    start_urls = ['http://163.com/']

    def parse(self, response):
        pass
