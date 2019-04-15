# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class UsstockPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
        cursor = db.cursor()
        sql = """INSERT INTO usstock values ('%s', '%s', '%s')"""%(item['name'], item['symbol'], item['no'])
        cursor.execute(sql)
        db.commit()
        db.close()
        return item
