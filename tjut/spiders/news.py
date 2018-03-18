# coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tjut.items import TjutItem
import requests
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
class MySpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['edu.cn']
    start_urls = ['http://news.tjut.edu.cn']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('yw', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('info', )), callback='parse_item'),
    )

    def parse_item(self, response):
        item = TjutItem()

        # response = etree.HTML(response.content)
        item['title'] = response.xpath('//*[@id="main"]/div[2]/div[1]/table/tbody/tr/td/form/table/tr[1]//text()').extract_first()
        # 动态请求点击数
        temp = response.xpath('//script[2]/text()').extract_first()
        wbnewsid = re.search(r"getClickTimes\('(\d*)','(\d*)','(.*?)',''\)", temp).group(1)
        owner = re.search(r"getClickTimes\('(\d*)','(\d*)','(.*?)',''\)", temp).group(2)
        count = requests.get(
            'http://news.tjut.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={}&owner={}'.format(
                wbnewsid, owner)).json()['wbshowtimes']
        list_one = response.xpath('//*[@id="main"]/div[2]/div[1]/table/tbody/tr/td/form/table//tr[2]/td/span/text()').extract()
        list_one.insert(-1, str(count))
        # 组成新闻详情
        item['details'] = ''.join(list_one)
        # 新闻内容及图片列表
        item['content'] = response.xpath('//*[@id="main"]/div[2]/div[1]/table/tbody/tr/td/form/table//tr[4]/td/div/div/p').extract()


        yield item