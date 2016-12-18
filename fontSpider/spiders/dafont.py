# -*- coding: utf-8 -*-
import scrapy


class DafontSpider(scrapy.Spider):
    name = "dafont"
    allowed_domains = ["dafont.com"]
    start_urls = ['http://dafont.com/']

    def parse(self, response):
        pass
