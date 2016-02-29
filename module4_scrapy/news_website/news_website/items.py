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
    img_desc  = scrapy.Field()

class NewsContentItem(scrapy.Item):
    title = scrapy.Field()
    provider = scrapy.Field()
    datetime = scrapy.Field()
    text_content = scrapy.Field()
    photo_src = scrapy.Field()
    photo_desc = scrapy.Field()