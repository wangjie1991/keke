# -*- coding: utf-8 -*-

import os
import urllib


class KekePipeline(object):
    
    def process_item(self, item, spider):

        path = item['path']
        if not os.path.exists(path):
            os.makedirs(path)

        wav_url = item['wav_url']
        wav_name = wav_url[wav_url.rfind('/')+1:]
        wav_name = path + '/' + wav_name
        wav_con = urllib.urlopen(wav_url)
        wav_byte = wav_con.read()
        with open(wav_name, 'wb') as wav_file:
            wav_file.write(wav_byte)

        lrc_url = item['lrc_url']
        lrc_name = lrc_url[lrc_url.rfind('/')+1:]
        lrc_name = path + '/' + lrc_name
        lrc_con = urllib.urlopen(lrc_url)
        lrc_byte = lrc_con.read()
        with open(lrc_name, 'wb') as lrc_file:
            lrc_file.write(lrc_byte)
        
        return item


