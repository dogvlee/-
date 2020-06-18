# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
from pymysql  import cursors

class doubanTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'douban',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = '''
             insert into  zfq(id,url,movie_name,cover,rate,directors,casts,movie_id) values(null ,%s,%s,%s,%s,%s,%s,%s)
            '''
            return self._sql
        return self._sql

    def process_item(self,item,spider):
        defer = self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(item['url'],item['movie_name'],item['cover'],item['rate'],item['directors'],item['casts'],item['movie_id']))


    def handle_error(self,error,item,spider):
        print('='*10+'error'+'='*10)
        print(error)
        print('='*10+'error'+'='*10)
