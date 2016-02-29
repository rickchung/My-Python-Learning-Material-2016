# -*- coding: utf-8 -*-

import scrapy

from news_website.items import NewsWebsiteItem

class PopNewsSpider(scrapy.Spider):
    name = "pop_news_spider"
    allowed_domains = ["udn.com"]

    # 定義要從哪個網址開始

    start_urls = [
        "http://udn.com/news/cate/6638",
    ]

    def parse(self, response):
        """ When response is received, this method will be called
        """
        # 過濾節點（根據我們要抓的網站）

        dt_list = response.xpath('//dt')   # 整個網站中所有的「dt」節點
        a_list = dt_list.xpath('a[h2]')    # 有 h2 子節點的 a 節點

        # 過濾內容

        article_url_list = a_list.xpath('@href')  # 取出 href attribute
        title_list = a_list.xpath('h2')           # h2 節點

        # 使用我們預先定義的 Items

        for i in a_list:
            new_item = NewsWebsiteItem()
            new_item['title'] = i.xpath('h2/text()')[0].extract()
            new_item['article_url'] = i.xpath('@href')[0].extract()
            yield new_item



