# coding=GBK
from django.http import HttpResponse


def page_2003(request):
    html = "<h1>���ǵ�һ��ҳ��</h1>"
    return HttpResponse(html)


def pagen(request, pg):
    html = "���ǵ�%s��ҳ�棡" % (pg)
    return HttpResponse(html)


def page_1(request):
    html = '���ǵ�һ��ҳ��'
    return HttpResponse(html)


def date(request, y, m, d):
    html = '����Ϊ:%s��%s��%s��' % (y, m, d)
    return HttpResponse(html)


def test(request,x):
    html='%s'%x
    return HttpResponse(html)