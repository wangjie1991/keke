# -*- coding: utf-8 -*-


class KekePipeline(object):
    
    def process_item(self, item, spider):

        path = item['path'] + '\n'
        wav_url = item['wav_url'] + '\n'
        lrc_url = item['lrc_url'] + '\n'
        
        with open('download.txt', 'a') as wf:
            wf.write(path)
            wf.write(wav_url)
            wf.write(lrc_url)
        
        return item


