# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouxinItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 现价格
    price = scrapy.Field()
    # 新车价格
    new_price = scrapy.Field()
    # 首付
    down_payment = scrapy.Field()
    # 月供
    monthly = scrapy.Field()
    # 使用年限
    use_time = scrapy.Field()
    # 行程
    travel = scrapy.Field()
    # 排放标准
    standard = scrapy.Field()
    # 排放
    discharge = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    pass
