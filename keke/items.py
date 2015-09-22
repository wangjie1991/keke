# -*- coding: utf-8 -*-

import scrapy

class KekeItem(scrapy.Item):
    path = scrapy.Field()
    wav_url = scrapy.Field()
    lrc_url = scrapy.Field()


