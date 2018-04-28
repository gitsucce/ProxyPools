#!/usr/bin/env python  
# encoding: utf-8 
# @Author    : w2n1ck
# @Time      : 2018/4/26 下午9:27
# @Introduce : 代理池是否用尽

class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr(u'oh~ 您的需求代理池已经满足不了啦～')