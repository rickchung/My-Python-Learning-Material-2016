# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from news_website.items import NewsContentItem

class PopNewsSpider(CrawlSpider):
    name = 'pop_news_crawlspider'
    allowed_domains = ['udn.com']
    start_urls = ['http://udn.com/news/cate/6638']

    rules = (
        Rule(LinkExtractor(allow=('news/story/.*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        # Debug log

        # self.logger.info('This is an item page: {url}'.format(url=response.url))

        # 找出關鍵節點

        story_body = response.xpath('//div[@id="story_body"]')
        story_body_info = story_body.xpath('.//div[@id="story_bady_info"]')

        # 清洗出資料

        title = story_body.xpath('.//h2/text()').extract()
        datetime = story_body_info.xpath('h3/text()').extract()
        provider = story_body_info.xpath('h3/span/text()').extract()
        text_content = '\n'.join([i for i in story_body.xpath('.//p/text()').extract()])
        photo_src = story_body.xpath('.//div[@class="photo_center photo-story"]//img/@src').extract()
        photo_desc = story_body.xpath('.//div[@class="photo_center photo-story"]//h4/text()').extract()

        # 塞入自定義的 Item 中

        news_item = NewsContentItem()
        news_item['title'] = title
        news_item['provider'] = provider
        news_item['datetime'] = datetime
        news_item['text_content'] = text_content
        news_item['photo_src'] = photo_src
        news_item['photo_desc'] = photo_desc

        return news_item
