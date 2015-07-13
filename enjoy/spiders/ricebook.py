
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from enjoy.items import EnjoyItem

class RicebookSpider(CrawlSpider):
    def getCount(i):
        if(i<10):
            return '000'+str(i)
        elif(i<100):
            return '00'+str(i)
        else:
            return '0'+str(i)


    name = "ricebook"
    allowed_domains = ["enjoy.ricebook.com"]
    start_urls = [
      # 'http://enjoy.ricebook.com/product/info?id=10711', #10002
    ]

    for i in range(1,1000,1):
        start_urls.append('http://enjoy.ricebook.com/product/info?id=1'+getCount(i))


    def parse(self, response):
        sel=Selector(response)
        item = EnjoyItem()

        item['title']= sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[1]/p[2]/text()').extract()
        item['type'] = sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[1]/p[1]/text()').extract()
        item['desc'] = sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[2]/text()').extract()
        item['price'] = sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[3]/span[1]/text()').extract()
        item['unit'] = sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[3]/span[2]/text()').extract()
        item['address'] = sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[6]/div[3]/ul/li[1]/p/text()').extract()
        item['tel'] = sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[6]/div[3]/ul/li[2]/p/text()').extract()
        item['purl'] = sel.xpath('//*[@id="gallery"]/div[3]/div[1]/ul/li[1]/a/@href').extract()
        isval = sel.xpath('//*[@id="productDetail"]/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/input').extract()
        if(isval):
            item['close']=1
        else:
            item['close']=0
        item['url'] = response.url
        if item['title']:
            return item
        else:
            return None
