import scrapy
from w3lib.http import basic_auth_header
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




class QuotesSpider(CrawlSpider):
    name = 'prox'

    allowed_domains = ['grubhub.com']
    start_urls = ['https://www.grubhub.com/', ]
    # scrapy.Request(
    #     url=start_urls, callback=parse,
    #      meta={'proxy': 'https://104.140.211.192:3128'},
    #      headers={
    #         'Proxy-Authorization': basic_auth_header(
    #             '', '','')
    #     }
    # )

    def parse(self, response):
#         item_list=[]
         self.log("i visited   "+ response.url)
#         # all_tags=response.xpath('//div[@class="quote"]/text')
#         # x = response.xpath('//a[@class="tag"]/text()').extract_first()
#         # y={
#         #     'author_name':response.xpath('/html/body/div/div/div/div/span/small/text()').extract(),
#         #     'text':response.xpath('/html/body/div/div/div/div/span/text()').extract(),
#         #     'tag': str(response.xpath('/html/body/div/div/div/div/div/a/text()').extract()).strip()
#         #
#         # }
         text=response.xpath('//*[@id="Site"]').extract_first()
         #text1=response.xpath('//*[@id="how-Why"]/div[1]/h3').extract()
         print(text)
         #print(text1)

#