# -*- coding: utf-8 -*-
import scrapy


class ZawCrawlSpider(scrapy.Spider):
    name = "zaw_crawl"
    allowed_domains = ["http://www.zhenai.com"]
    start_urls = ['http://http://www.zhenai.com/']

    def parse(self, response):
        pass
