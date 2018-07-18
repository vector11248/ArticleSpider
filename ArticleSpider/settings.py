# -*- coding: utf-8 -*-

# Scrapy settings for ArticleSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

<<<<<<< HEAD
import os

=======
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c
BOT_NAME = 'ArticleSpider'

SPIDER_MODULES = ['ArticleSpider.spiders']
NEWSPIDER_MODULE = 'ArticleSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ArticleSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
<<<<<<< HEAD
ROBOTSTXT_OBEY = False
=======
ROBOTSTXT_OBEY = False #默认是True，jobbole视频是False
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ArticleSpider.middlewares.ArticlespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ArticleSpider.middlewares.ArticlespiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
<<<<<<< HEAD
ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    # scrapy 在py lib 包里
     'scrapy.pipelines.images.ImagesPipeline':1,
    # 'ArticleSpider.pipelines.ArticleImagePipeline':1,
    # 'ArticleSpider.pipelines.JsonWithEncodingPipeline':2,
    'ArticleSpider.pipelines.JsonExporterPipeline':3,
    'ArticleSpider.pipelines.MysqlPipeline': 2,
    # 'ArticleSpider.pipelines.MysqlTwistedPipeline': 2,


}

#去item里找这个字段,这个写法是固定的
IMAGES_URLS_FIELD = "front_image_url"
#设置一个图片下载的目录，写法固定

project_dir = os.path.abspath(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(project_dir,'images')

#过滤掉特殊的图片
# IMAGES_MIN_HEIGHT = 100
# IMAGES_MIN_WIDTH = 100

=======
#ITEM_PIPELINES = {
#    'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
#}
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
<<<<<<< HEAD


MYSQL_HOST = "localhost"
MYSQL_DBNAME = "Jobbole_spider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
=======
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c
