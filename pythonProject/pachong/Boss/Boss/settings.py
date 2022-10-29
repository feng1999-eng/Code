# Scrapy settings for Boss project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Boss'

SPIDER_MODULES = ['Boss.spiders']
NEWSPIDER_MODULE = 'Boss.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


LOG_LEVEL = "ERROR"
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#     'Cookies':'__snaker__id=YqZk3nAiXnjH8mmH; acw_tc=0a099d6e16580468692683944e017a4856de0438bdc3d0c042fcbdc8df10cb; lastCity=101110100; __zp_seo_uuid__=9ac79761-c96d-4036-a12f-8f0b7fee9d43; __g=-; wd_guid=cbfeaa33-f708-40d7-b19f-34453216b92e; historyState=state; _bl_uid=yLl3z5gjpOn2z3aOav6541zoOv1b; __c=1658046871; __l=r=https%3A%2F%2Fwww.google.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3Dc%252B%252B%26city%3D101110100&s=3&g=&friend_source=0&s=3&friend_source=0; __a=30919465.1658046871..1658046871.3.1.3.3; __zp_stoken__=cb6cdC1tcRSBtbXJ0LTgeQS1tCmkkD0lrcWEGQng3XHcwQVoYbGEoaxA0F1lUfBpHGn9uEi19KyIJJlc8PmMpW3k9WyIYZEAUemIgcxlHEy9fGAFnEx0IU1t4cXMvFHgnWEZcbC13VEA2PA0%3D; gdxidpyhxdE=dHWhBBX%5CnmYstNmvarz2x0wQqnf%2BlyIs0HcZndY7OS2d4r%5COrzW2ZNR4wJWSjGIZEwpUb%2BWT9TyYhELwUdVebnwNu8%2BueJsHx%2FEeWup62ZitRWHlgSs79PthETMC65WKNXtzT60P02iPbIzqgM%2FM%2FoKrE%2FxDZvkQW%5CRV7%5C1e%2FVPGklWw%3A1658048514967; _9755xjdesxxd_=32; YD00951578218230%3AWM_NI=er7Si4K9jB4pHyVCCy8NY5TB6aBgoVaWPLjAIUX084GQvhThuV8m01g9kUDZG6qF8f%2Bqh%2FKdAlHfyXYTURDUrBY%2F9CC%2Fwcdhx8SR4L4dUiux1qYqRdrAkvtzWbfyVz%2B7VWw%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeacc880a38efaa8e450aab48fa2d84a829f9e82d560869da0bbf072bb9ca696e92af0fea7c3b92aa7aef9b4ec4089e7a6a3b77c8ca79aa4c273fc9297d6d74af6bf8e88ee5ea389a0ade94b8b8b98d1bb40858fba89d764b78af88eb33ba5e7a5b6c75285eabfa7bb6ee9afa8d0ca7083b48887fc549b8c9bb3c75fb29e97d0bc4981f1b984e764bce89db3b748f8bc9b8af874f3af9792d170b29fa597f77295beaa9ad572e9e99ab8f637e2a3; YD00951578218230%3AWM_TID=X7gY8bmbR4VEVVABBEOVXRTbdzmnG2vj'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Boss.middlewares.BossSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Boss.middlewares.BossDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Boss.pipelines.BossPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
