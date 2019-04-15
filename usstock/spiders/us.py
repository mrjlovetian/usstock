# -*- coding: utf-8 -*-
import scrapy
from usstock.items import UsstockItem
import json

class UsSpider(scrapy.Spider):
    name = 'us'
    allowed_domains = ['163.com']
    baseUrl = 'http://quotes.money.163.com/us/service/usrank.php?host=/us/service/usrank.php&page=0&query=UPDATE:_exists_true;PRICE:_exists_true;typename:nasdaq&fields=no,SYMBOL,NAME,PRICE,UPDOWN,PERCENT,WEEK52_HIGH,WEEK52_LOW,TCAP,PE&count=2&type=query&req=11010'
    start_urls = [baseUrl]

    def parse(self, response):
        # body = json.loads(response.body)
        # print ('........................', body)
        usstocks = json.loads(response.body)['list']
        i = 1
        for usstock in usstocks:
            item = UsstockItem()
            item['name'] = usstock['NAME']
            item['symbol'] = usstock['SYMBOL']
            item['no'] = str(i)
            item['typename'] = 'nasdaq'
            i += 1
            yield item
        
        
