# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaiwanPresident2016Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    region_name     = scrapy.Field()
    region_number   = scrapy.Field()
    can_name        = scrapy.Field()
    can_number      = scrapy.Field()
    can_vote        = scrapy.Field()

    pass
