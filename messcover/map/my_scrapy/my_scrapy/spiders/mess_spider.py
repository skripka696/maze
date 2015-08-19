from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from ..items import MyScrapyItem
from scrapy.contrib.linkextractors import LinkExtractor
from ..actions import start_url
from map.models import My_Tree

class Mess(CrawlSpider):
    My_Tree.objects.all().delete()
    name = 'mess'
    allowed_domains = ["localhost"]
    start_urls = [start_url(), ]
    rules = [
        Rule
        (
            LinkExtractor(
                restrict_xpaths=('//a[@class="next"]')),
            callback = 'parse_item',
            follow = True,
        )
    ]

    def parse_item(self, response):
        hxs = response
        item = MyScrapyItem()
        item['name'] = hxs.xpath('//*[@id="content"]/a/button/text()').extract()
        item['url'] = response.url
        item['link'] = hxs.xpath('//a/@href').extract()
        s = My_Tree(url=item['url'], link=item['link'], name=item['name'])
        s.save()
        print item
        return item
