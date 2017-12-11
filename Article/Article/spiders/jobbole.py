# -*- coding: utf-8 -*-
from urllib import parse

import scrapy


from scrapy.http import Request
from Article.items import ArticleItem



from scrapy_redis.spiders import RedisSpider

# class JobboleSpider(scrapy.Spider):
class JobboleSpider(RedisSpider):
    name = 'jobbole'
    redis_key = 'jobbole:start_urls'
    # start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        Article = ArticleItem()
        for article in response.xpath('//*[@id="archive"]/div')[0:20]:
            title = article.xpath('div[2]/p[1]/a[1]/text()').extract_first()
            lead = article.xpath('div[2]/span/p/text()').extract_first()
            Article['title'] = title
            Article['lead'] = lead
            yield Article
        next_url = response.xpath("//a[@class='next page-numbers']/@href").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)