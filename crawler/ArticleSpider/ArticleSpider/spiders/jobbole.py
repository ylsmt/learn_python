# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbple.com']
    start_urls = ['http://blog.jobbple.com/']

    def parse(self, response):
        pass
