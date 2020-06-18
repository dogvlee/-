# -*- coding: utf-8 -*-
import scrapy

import re
from douban.items import DoubanItem
class DoubanDemoSpider(scrapy.Spider):
    name = 'douban_demo'
    # allowed_domains = ['movie.douban']
    start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=600&genres=%E6%83%85%E8%89%B2']

    def parse(self, response):
        # genres=[,'',

       #        '%E6%88%98%E4%BA%89'：6600,'%E8%A5%BF%E9%83%A8','%E5%A5%87%E5%B9%BB','%E5%86%92%E9%99%A9','%E7%81%BE%E9%9A%BE','%E6%AD%A6%E4%BE%A0'：1400,'%E6%83%85%E8%89%B2']
        # 爱情：9980 科幻：动画：9220 悬疑：9940，惊悚，恐怖9960 同性:2100 音乐9000 歌舞：8000
        # supenses=['%E6%82%AC%E7%96%91','%E6%83%8A%E6%82%9A','%E6%81%90%E6%80%96'] 悬疑：9940，惊悚，恐怖9960
        features=['%E5%89%A7%E6%83%85']
        # carton = ['%E5%8A%A8%E7%94%BB']
        # musices=['%E9%9F%B3%E4%B9%90','%E6%AD%8C%E8%88%9E']
        biography = ['%E4%BC%A0%E8%AE%B0']
        gay = ['%E5%90%8C%E6%80%A7']
        # Sciences=['%E7%A7%91%E5%B9%BB','%E5%A5%87%E5%B9%BB']
        war = ['%E6%88%98%E4%BA%89']  # 6600
        Disaster = ['%E7%81%BE%E9%9A%BE']
        west = ['%E8%A5%BF%E9%83%A8']
        comedy = ['%E5%96%9C%E5%89%A7']
        Swordsman = ['%E6%AD%A6%E4%BE%A0']
        sexy = ['%E6%83%85%E8%89%B2']


        history=['%E5%8E%86%E5%8F%B2'] #5000

        Crime=['%E7%8A%AF%E7%BD%AA']



        # for Science in Crime:
        for x in range(0,200,20):
            page = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start='+str(x)+'&genres=%E6%83%85%E8%89%B2&countries=%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF'
            yield scrapy.Request(url=page, callback=self.parse_star_list,meta={'page':page,'x':x})



    def parse_star_list(self,response):
        contents = eval(response.text).get("data")
        ajax_url=response.meta.get('page')
        x=response.meta.get('x')
        if contents:
            for content in contents:
                url_row = content['url']
                url = re.sub(r'\\', "", url_row)
                cover_row = content['cover']
                cover = re.sub(r'\\', "", cover_row)
                rate = content['rate']
                movie_name = content['title']
                directors = str(content['directors'])
                casts = str(content['casts'])
                movie_id = content['id']
                item=DoubanItem(url=url,cover=cover,rate=rate,movie_name=movie_name,directors=directors,casts=casts,movie_id=movie_id)


                yield item


        else:

            print(x)
            print(ajax_url)


