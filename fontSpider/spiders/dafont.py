# -*- coding: utf-8 -*-
import scrapy


class DafontSpider(scrapy.Spider):
    name = "dafont"
    allowed_domains = ["dafont.com"]
    start_urls = ['http://dafont.com/new.php']

    def parse(self, response):
        print "--------------------------------------------------"
        for href in response.css('a.dl::attr(href)').extract():
            print "[hit:" + href + "]"
            #超链接的title为Keyboard shortcut: Right arrow
        next_page = response.css("a[title='Keyboard shortcut: Right arrow']::attr(href)").extract_first()
        print "next_page" + next_page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        pass
