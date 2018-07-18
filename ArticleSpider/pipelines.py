# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
<<<<<<< HEAD
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi
import codecs
import json
import MySQLdb
import MySQLdb.cursors


=======
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item
<<<<<<< HEAD

#定制自己的pipeline
class ArticleImagePipeline(ImagesPipeline):
    #结果存放在results里面
    def item_completed(self, results, item, info):
        for ok,value in results:
            image_file_path = value["path"]
        item["front_image_path"]=image_file_path
        return item
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json','w',encoding="utf-8")
    def process_item(self, item, spider):
        #一定要带着ensure_ascii=False，否则正文显示不正常
        lines = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()

class JsonExporterPipeline(object):
    #调用scrapy提供的Json Exporter导出json文件
    def __init__(self):
        self.file = open('articleExporter.json','wb')
        self.exporter = JsonItemExporter(self.file,encoding="utf-8",ensure_ascii=False)
        self.exporter.start_exporting()
        self.exporter._beautify_newline()
    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost','root','root','Jobbole_spider',charset="utf8",use_unicode=True)

        #对数据库的操作都是用cursor
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        insert_sql = """
            insert into jobbole_article(header,approval,url_object_id,bookmark,
            comment_num,url,create_time,front_image_url)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql,(item["header"],item["approval"],item["url_object_id"]
                                        ,item["bookmark"],item["comment_num"]
                                        ,item["url"],item["create_time"],
                                        item["front_image_url"]))
        self.conn.commit()

class MysqlTwistedPipeline(object):

    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        dbparams = dict(
            host=settings["MYSQL_HOST"],
            db = settings[" MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            pwd = settings["MYSQL_PASSWORD"],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )


        # 注意**代表一个可变化的参数
        dbpool = adbapi.ConnectionPool("MySQLdb",**dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handler_error) #处理异常


    def handler_error(self,failure):
        print(failure)

    def do_insert(self,cursor,item):
        #执行具体的插入操作
        insert_sql = """
                    insert into jobbole_article(header,approval,url_object_id,bookmark,
                    comment_num,url,create_time,front_image_url)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """
        cursor.execute(insert_sql, (item["header"], item["approval"], item["url_object_id"]
                                         , item["bookmark"], item["comment_num"]
                                         , item["url"], item["create_time"],
                                         item["front_image_url"]))










=======
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c
