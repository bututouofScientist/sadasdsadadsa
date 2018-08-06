from urllib import parse

from django.http import HttpResponse
from django.shortcuts import render
import datetime


def set_cookie(request):
    response = HttpResponse('测试设置cookie')
    t = request.GET.get('type', 1)  # t是字符串
    t = int(t)

    if t == 1:
        c = parse.quote('上海尚学堂', encoding='utf-8')
        response.set_cookie('normal', c)
    elif t == 2:
        response.set_cookie('max_age_cookie', '123456', max_age=15)
    elif t == 3:
        response.set_cookie('expire_cookie', '123456', max_age=15, expires=datetime.datetime(2018, 8, 1, 15, 23, 59))
    elif t == 4:
        response.set_cookie('path_cookie', '123456', path='/cookie/read_cookie')
    return response