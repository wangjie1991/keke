# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from keke.spiders.linkfilter import LinkFilter
from keke.items import KekeItem
from keke import settings


class KekeSpider(CrawlSpider):
    name = 'keke'
    allowed_domains = ['www.kekenet.com']
    start_urls = ['http://www.kekenet.com/broadcast/']
    linkfilter = LinkFilter('keke')
    
    rules = [Rule(LinkExtractor(allow=(r'http://www\.kekenet\.com/mp3/[0-9/]*\.shtml')), 
                  callback='parse_item', follow=False, process_links=linkfilter.html_filter),
             Rule(LinkExtractor(allow=(r'http://www\.kekenet\.com/broadcast/.*')), 
                  process_links=linkfilter.index_filter)]
    
    def parse_item(self, response):
        item = KekeItem()

        path = response.url
        path = path.lstrip('http://www.kekenet.com/mp3/')
        path = path.rstrip('.shtml')
        item['path'] = '%s/%s' % (settings.KEKE_STORE, path)

        txt = response.body
        wav_tag = 'mp3下载地址'
        wav_index1 = txt.find(wav_tag)
        lrc_tag = '字幕下载地址'
        lrc_index1 = txt.find(lrc_tag)

        if ((-1 == wav_index1) or (-1 == lrc_index1)):
            return None

        # 判断是否在注释内
        wav_cmt1 = txt.rfind('<!--', 0, wav_index1)
        wav_cmt2 = txt.find('-->', wav_cmt1)
        lrc_cmt1 = txt.rfind('<!--', 0, lrc_index1)
        lrc_cmt2 = txt.find('-->', lrc_cmt1)
        # tag在注释中
        if (wav_index1 < wav_cmt2) or (lrc_index1 < lrc_cmt2):
            return None

        wav_index2 = txt.rfind('http', 0, wav_index1)
        wav_index3 = txt.find('"', wav_index2, wav_index1)
        item['wav_url'] = txt[wav_index2 : wav_index3]

        lrc_index2 = txt.rfind('http', 0, lrc_index1)
        lrc_index3 = txt.find('"', lrc_index2, lrc_index1)
        item['lrc_url'] = txt[lrc_index2 : lrc_index3]
        
        return item


