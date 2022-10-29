# coding=GBK
from django.http import HttpResponse


def page_2003(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def pagen(request, pg):
    html = "这是第%s个页面！" % (pg)
    return HttpResponse(html)


def page_1(request):
    html = '这是第一个页面'
    return HttpResponse(html)


def date(request, y, m, d):
    html = '生日为:%s年%s月%s日' % (y, m, d)
    return HttpResponse(html)


def test(request,x):
    html='%s'%x
    return HttpResponse(html)