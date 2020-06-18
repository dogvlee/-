# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    movie_name = scrapy.Field()
    url=scrapy.Field()
    cover=scrapy.Field()
    rate=scrapy.Field()

    directors =scrapy.Field()
    casts =scrapy.Field()
    movie_id =scrapy.Field()

class ajaxItem(scrapy.Item):
    ajax_url=scrapy.Field()
    x=scrapy.Field()
