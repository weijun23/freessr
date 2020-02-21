#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import time
import dryscrape
import base64

# 定义爬虫类
class Spider():
    def __init__(self):
        #self.url = 'https://free-ss.site'
        #self.headers = {
        #    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        #}
        #r = requests.get(self.url,headers=self.headers)
        #r.encoding = r.apparent_encoding
        #self.html = r.text

        file_obj = open("./html.txt")
        text = file_obj.read()
        #print text
        self.html = text

    def lxml_find(self):
        #用lxml解析
        start = time.time()                     # 三种方式速度对比
        selector = etree.HTML(self.html)        # 转换为lxml解析的对象
        titles = selector.xpath('//div[@id="tbss_wrapper"]//tr/td/text()')    # 这里返回的是一个列表

        ss_result="MAX=3\n"
        #ss://Method:Password@Address:Port
        for i in range(0, len(titles), 7):
            ss_result=ss_result+"ss://"+titles[i+3]+":"+titles[i+4]+"@"+titles[i+1]+":"+titles[i+2]+"\n"
        print ss_result
        text=base64.b64encode(ss_result)
        #print text
        file_obj = open("./ss", "w")
        file_obj.write(text)

    def BeautifulSoup_find(self):
        #用BeautifulSoup解析
        start = time.time()
        soup = BeautifulSoup(self.html, 'lxml')   # 转换为BeautifulSoup的解析对象()里第二个参数为解析方式
        titles = soup.find_all('li', class_='list-item')
        for each in titles:
            title = each['data-title']
            print(title)
        end = time.time()
        print('BeautifulSoup耗时', end-start)

    def re_find(self):
        #用re解析
        start = time.time()
        titles = re.findall('data-title="(.+)"',self.html)
        for each in titles:
            print(each)
        end = time.time()
        print('re耗时', end-start)

if __name__ == '__main__':
    #dryscrape.start_xvfb()
    #session_req=dryscrape.Session()
    #session_req.visit('https://free-ss.site') #请求页面
    #response=session_req.body() #网页的文本
    #print response

    spider = Spider()
    spider.lxml_find()
    #spider.BeautifulSoup_find()
    #spider.re_find()
