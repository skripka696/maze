from twisted.internet import reactor
from scrapy import log, signals
from map.my_scrapy.my_scrapy.spiders.mess_spider import Mess
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings


def run_spider():
    spider = Mess()
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    log.start()
    # the script will block here until the spider_closed signal was sent

    reactor.run()
#
# from scrapy.crawler import Crawler
# from map.my_scrapy.my_scrapy.spiders.mess_spider import Mess
# from scrapy import log, signals
# from twisted.internet import reactor
# from billiard import Process
# from scrapy.utils.project import get_project_settings
#
#
# class UrlCrawlerScript(Process):
#         def __init__(self, spider):
#             Process.__init__(self)
#             settings = get_project_settings()
#             self.crawler = Crawler(settings)
#             self.crawler.configure()
#             self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
#             self.spider = spider
#
#         def run(self):
#             self.crawler.crawl(self.spider)
#             self.crawler.start()
#             log.start()
#             reactor.run(installSignalHandlers=0)
#
#
# def run_spider():
#     spider = Mess()
#     crawler = UrlCrawlerScript(spider)
#     crawler.start()
#     crawler.join()