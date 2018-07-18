# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
<<<<<<< HEAD

class ArticleItem(scrapy.Item):
    header = scrapy.Field()
    create_time = scrapy.Field()
    approval = scrapy.Field()#赞同数
    bookmark = scrapy.Field()#收藏数
    comment_num = scrapy.Field()#评论数


    #页面是从哪一个ｕrl过来的
    url = scrapy.Field()
    #通过md5转换为一个唯一的且定长的url
    url_object_id = scrapy.Field()

    #文章封面图
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()

=======
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c
