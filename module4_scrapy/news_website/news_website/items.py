# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsWebsiteItem(scrapy.Item):
    """ Define what data is we want
    """
    title       = scrapy.Field()  # News title
    article_url = scrapy.Field()  # News URL
    author      = scrapy.Field()  # News author
    provider    = scrapy.Field()  # News provider
    datetime    = scrapy.Field()  # Uploaded time
    content     = scrapy.Field()  # Text content

    img_urls  = scrapy.Field()      # Images 
    youtube_urls = scrapy.Field()   # YouTube
