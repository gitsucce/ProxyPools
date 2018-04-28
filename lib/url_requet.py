#!/usr/bin/env python  
# encoding: utf-8 
# @Author    : w2n1ck
# @Time      : 2018/4/26 下午4:29
# @Introduce : requests请求
import random
import requests
import sys, os
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from requests.exceptions import ConnectionError
from conf.config import _config

UA = _config()
base_headers = {
    'User-Agent': random.choice(UA['USER_AGENTS']),
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}


def get_page(url, options={}):
    """
    抓取代理
    """
    headers = dict(base_headers, **options)
    try:
        response = requests.get(url, headers=headers)
        print('抓取成功 >>> ', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('抓取失败 >>> ', url)
        return None
