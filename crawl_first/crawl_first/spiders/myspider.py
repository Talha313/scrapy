# -*- coding: utf-8 -*-
import scrapy
from w3lib.http import basic_auth_header
import scrapy
import requests
import request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from bs4 import BeautifulSoup
from scrapy import Selector
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.item import Item
from scrapy import  Selector
from scrapy.core.downloader.webclient import _parse
#_parse('https://username:password@104.140.211.192:3128')
#('https', 'username:password@104.140.211.192', '104.140.211.192', 3128, '/


# proxy = request.meta.get('proxy')
# if proxy:
#   _, _, proxyHost, proxyPort, proxyParams = _parse(proxy)
#   scheme = _parse(request.url)[0]
#   proxyHost = to_unicode(proxyHost)
#   omitConnectTunnel = b'noconnect' in proxyParams
#   if scheme == b'https' and not omitConnectTunnel:
#     proxyConf = (proxyHost, proxyPort,
#                  request.headers.get(b'Proxy-Authorization', None))
#     return self._TunnelingAgent(reactor, proxyConf,
#                                 contextFactory=self._contextFactory, connectTimeout=timeout,
#                                 bindAddress=bindaddress, pool=self._pool)

# proxies = {
#   'http': 'http://104.140.211.192:3128',
#   'https': 'http://206.214.93.246:3128',
# }
# #requests.get('http://grubhub.com', proxies=proxies)
# response = requests.get('http://grubhub.com',proxies=proxies)
#
# print(response.json())

#class QuotesSpider(CrawlSpider):

 #   name = 'quotes'

  #   allowed_domains = ['grubhub.com']
   #  start_urls = ['https://www.grubhub.com/',]
#                   #'https://quotes.toscrape.com/page/2',]
#                   #'http://quotes.toscrape.com/'
#     # custom_settings = {
#     #          'FEED_FORMAT': 'csv',
#     #          'FEED_URI': 'test.csv',
#     #      # 'JOBDIR': '/Data/Work/SamaritanTech/PythonProjects/lipseys_scraper/core/core/spiders/state_job'
#     #          }
#
#     #rules = (
#          # Extract links matching 'item.php' and parse them with the spider's method parse_item
#          #Rule(LinkExtractor(allow=('\*',)), callback='parse_item'),
#
#          #Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="next"]',)), callback="parse_items",  follow=True),
#      #    Rule(LinkExtractor(allow=('/\w*/\w')), callback='parse_item'),
#      #    Rule(LinkExtractor(allow=('.*',))),
#      # )
    # def parse(self, response):
#         item_list=[]
     #    self.log("i visited   "+ response.url)
#         # all_tags=response.xpath('//div[@class="quote"]/text')
#         # x = response.xpath('//a[@class="tag"]/text()').extract_first()
#         # y={
#         #     'author_name':response.xpath('/html/body/div/div/div/div/span/small/text()').extract(),
#         #     'text':response.xpath('/html/body/div/div/div/div/span/text()').extract(),
#         #     'tag': str(response.xpath('/html/body/div/div/div/div/div/a/text()').extract()).strip()
#         #
#         # }
      #   text=response.xpath('/html/head/title/text()').extract()
       #  print(text)
#         item_dict={}
        # for quote in response.css('div.quote'):
        #     text = quote.css("span.text::text").extract_first()
        #     author = quote.css("small.author::text").extract_first()
        #     tags = quote.css("div.tags a.tag::text").extract()
        #     item_dict={
        #         'text':text,
        #         'author':author,
        #         'tags':tags
        #     }
        #     if item_dict not  in item_list:
        #         item_list.append(item_dict)
            #print(item_dict)
            #print(dict(text=text, author=author, tags=tags))
      #  print(item_list)

           # f.write(y['author_name'])

        #x=response.css('a.tag::text()').extract_first()
        #print(y['author_name'], "Data ye hai")


#//h1[@class="page-heading"]/text()
#/html/body/div/div[2]/div[1]/div[1]/div