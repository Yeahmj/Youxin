# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Youxin.items import YouxinItem

# 1.导入类
from scrapy_redis.spiders import RedisCrawlSpider

# 2, 修改类的继承
# class YouxinSpider(CrawlSpider):
class YouxinSpider(RedisCrawlSpider):
    name = 'youxin'

    # 3, 注销允许的域和起始的url
    # allowed_domains = ['www.xin.com']
    # start_urls = ['https://www.xin.com/shanghai/sn_l6/i1/?channel=baidu&mediaid=1']

    # 4, redis_key
    redis_key = 'tocar'

    # ---- 5 编写 __init__ ，获取允许的域
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(YouxinSpider, self).__init__(*args, **kwargs)

    rules = (
        # 列表页
        Rule(LinkExtractor(allow=r'/shanghai/sn_l6/i\d+/'), follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'//www\.xin\.com/\D+/che\d+\.html$'), callback='parse_item'),
    )

    def parse_item(self, response):
        # print(response.url)
        # 创建存储容器
        item = YouxinItem()

        # 抽取数据
        item['title'] = response.xpath('//div[@class="cd_m_info_it2"]/div[@class="cd_m_h cd_m_h_zjf"]/span/text()').extract_first().strip()
        item['price'] = response.xpath('/html/body/div[2]/div[2]/div[2]/p/span[1]/b/text()').extract_first()
        item['new_price'] = response.xpath('/html/body/div[2]/div[2]/div[2]/p/span[2]/span[1]/b/text()').extract_first()
        item['down_payment'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/span[1]/text()').extract_first()
        item['monthly'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/span[2]/text()').extract_first()
        item['use_time'] = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[1]/span[1]/text()').extract_first().strip()
        item['travel'] = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[2]/a/text()').extract_first().strip()
        item['standard'] = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[3]/span[1]/text()').extract_first()
        item['discharge'] = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[4]/span[1]/text()').extract_first() #no ce
        item['city'] = response.xpath('/html/body/div[2]/div[2]/div[2]/ul/li[5]/span[1]/text()').extract_first() #no ce
        print(item)

        # 返回给引擎
        yield item















