# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

# 如果需要url拼接则如下
from urllib import parse

#import　item　的数据
from ArticleSpider.items import ArticleItem

from ArticleSpider.utils.common import get_md5
import datetime

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts']

    def parse(self, response):

        #获取所有文章的url
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:

            #交给scrapy进行下载
            # yield  Request(url=post_url,callback=self.parse_detail)
            #如果需要url拼接则调用如下函数

            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":image_url},callback=self.parse_detail)
            print(post_url)

        # .next.page-numbers 中间没有空格，则代表这两个类指向的是同一个，如果中间有空格，则
        #  存在层级关系
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            # yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse_detail)
            yield Request(url=next_url,callback=self.parse)

    #该函数提取具体页面当中的字段
    def parse_detail(self,response):

        #item 初始化
        article_item = ArticleItem()

        #通过meta获取front_image_url
        #文章封面图
        front_img_url = response.meta.get("front_image_url","")

        #标题
        header = response.xpath("//div[@class='entry-header']/h1/text()")
        header = header.extract_first()
        # header = header.extract()[0]
        # print(header)
        #创建时间
        create_time = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()")
        create_time = create_time.extract_first()
        if create_time != None:
            create_time = create_time.strip().replace("·","").strip()
        # print(create_time)
        #赞同数
        approval = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()")
        approval = approval.extract_first()

        # print(approval)
        #收藏数
        bookmark = response.xpath("//span[contains(@class,'bookmark-btn')]/text()")
        if bookmark.extract_first() != None:
            bookmark_match = re.match("\s(\d+)\s收藏",bookmark.extract()[0])
            if bookmark_match:
                bookmark = int(bookmark_match.group(1))
            else:
                bookmark = 0
        else:
            bookmark = 0
        #评论数
        comment_num = response.xpath("//a[@href='#article-comment']/span/text()")
        if comment_num.extract_first() != None:
            comment_match = re.match("\s(\d+)\s评论",comment_num.extract()[0])
            if comment_match:
                comment_num = int(comment_match.group(1))
            else:
                comment_num = 0
        else:
            comment_num = 0

        print(bookmark)
        print(comment_num)


        article_item["header"] = header
        article_item["url"] = response.url
        article_item["url_object_id"] = get_md5(response.url)
        article_item["front_image_url"] = [front_img_url]

        try:
            create_time = datetime.datetime.strptime(create_time,"%Y/%m/%d").date()
        except Exception as e:
            create_time = datetime.datetime.now().date()

        article_item["create_time"] = create_time
        article_item["approval"] = approval
        article_item["bookmark"] = bookmark
        article_item["comment_num"] = comment_num

        yield article_item

        # pass
