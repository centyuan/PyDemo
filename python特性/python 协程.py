# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/5 15:39
import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 ok'

def produce(c):
    c.next()

