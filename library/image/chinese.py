#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
simple module to translate English to Chinse, Chinese to English
'''

# API key：701380394
# keyfrom：youdao-python

from __future__ import print_function, unicode_literals
import json
import sys


try:
    # compatible for python2
    from urllib import urlencode
    from urllib2 import urlopen
except ImportError:
    # compatible for python3
    from urllib.parse import urlencode
    from urllib.request import urlopen


URL = "http://fanyi.youdao.com/openapi.do?" + \
      "keyfrom=youdao-python&key=701380394" + \
      "&type=data&doctype=json&version=1.1&"

class Chinese_Translator:
    def fetch(self, query_str):
        '''
        use youdao api to get json result of translation
        '''
        #print("查询单词：", query_str.strip())
        query = {
            'q': query_str.strip()
        }
        url = URL + urlencode(query)
        response = urlopen(url, timeout=3)
        html = response.read().decode("utf-8")
        return html


    def print_translate(self, translate):
        '''
        print translation
        '''
        #print("有道翻译：", end='')
        for trans in translate:
            print(trans, end='')
        print("")


    def parse(self, html):
        '''
        parse the json result to what user could read
        '''
        translation = json.loads(html)
        if translation.get('errorCode') == 0:
            if 'translation' in translation:
                #print_translate(translation.get('translation'))
                return translation.get('translation')[0]


    def sanitize_arg(self, query_str):
        '''
        sanitize the argument first
        '''
        if hasattr(query_str, "decode"):
            result = query_str.decode("utf8")
            result = result.strip("'")
            result = result.strip('"')
            result = result.encode("utf-8")
        else:
            result = query_str.strip("'").strip('"')
        return result

    def translate(self, text=''):
        youdao_json = self.fetch(self.sanitize_arg(text))
        return self.parse(youdao_json)    


#print(Chinese_Translator().translate(text='旁边的阿班突然搜住她的手'))
