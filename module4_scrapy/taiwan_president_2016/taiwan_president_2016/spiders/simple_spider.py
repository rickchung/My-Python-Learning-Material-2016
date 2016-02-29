# -*- coding: utf-8 -*-

import scrapy

class SimpleSpider(scrapy.Spider):
    name = 'simple_spider'
    allowed_domains = ["cec.gov.tw"]
    start_urls = [
        'http://www.cec.gov.tw/zh_TW/P1/n100000100000000.html',
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)