# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112125']

    def parse(self, response):
        # re_selector=response.xpath('//*[@id="post-113930"]/div[1]/h1/text()')
        #通过id或者class来定位xpath,两者都行，只要是全局唯一的，能够准确定位。
        #response.xpath返回的是一个selector对象。该对象有许多方法，包括extract()
        #Scrapy文档http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html#spider

        #标题
        header=response.xpath('//*[@class="entry-header"]/h1/text()')
        header = header.extract()[0]
        #创建时间
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')
        create_date=create_date.extract()[0].strip().replace("·","").strip()
        #赞同数
        approval = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()')
        approval = approval.extract()[0]
        #收藏数
        bookmark = response.xpath('//span[contains(@class,"bookmark-btn")]')
        if bookmark.re("\s(\d+)\s收藏"):
            bookmark = bookmark.re("\s(\d+)\s收藏")[0]
        else:
            bookmark = 0
        #评论数
        comment = response.xpath('//a[@href="#article-comment"]/span/text()')
        if comment.re("\s(\d+)\s评论"):
            comment = comment.re("\s(\d+)\s评论")[0]

        pass
