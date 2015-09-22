# -*- coding: utf-8 -*-

import os


class KekePipeline(object):
    
    def process_item(self, item, spider):
        path = item['path']
        wav_url = item['wav_url']
        lrc_url = item['lrc_url']

        if not os.path.exists(path):
            os.makedirs(path)
        wav_name = wav_url[wav_url.rfind('/')+1:]
        lrc_name = lrc_url[lrc_url.rfind('/')+1:]

            
            with open(path, 'w') as fout:
                if 'title' in item and item['title'] != '':
                    s = item['title'] + '\n'
                    fout.write(s.encode('utf-8'))
                fout.write(text.encode('utf-8'))
        
        return item
