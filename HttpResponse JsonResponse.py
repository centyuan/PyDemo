# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/28 10:26

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
# 一:
def index(request):
    data = {
        "name": "wuzhao",
        "age": 18
    }
    return HttpResponse(json.dumps(data))
#返回的Content-Type：是text/html，也就是字符串类型的返回，
# 所以这段返回值并不是一个标准的json数据，是一个长得像json数据的字符串，当然可以通过工具直接转换为json

# 二；
def index(request):
    data = {
        "name": "wuzhao",
        "age": 19
    }
    return HttpResponse(json.dumps(data),content_type="application/json")

# 三：
def index(requset):
    data = {
        "name": "wuzhao",
        "age": 18
    }
    return JsonResponse(data)
    # 同时支持list,JsonResponse在抛出列表的时候需要将safe设置为False safe=False
    # listdata = [1,2,3,4,5]
    # return JsonResponse(listdata,safe=False)

