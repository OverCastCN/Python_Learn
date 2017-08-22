#coding:utf-8
import json
import requests
from requests import Request,Session

"""
在session中规定了一些代理，时间，认证等信息
在prepared Request准备好的请求中定义了消息的body,headers,auth等
最后将这个prepared Request发出，得到response，response中含有text,json等信息
"""


def hard_request():
    s = Session()
    headers = {'User-Agent':'fake1.3.4'}#虚构的heard信息
    req = Request('GET','https://api.github.com/user/emails',auth=('imoocdemo','imoocdemo123'),headers=headers)
    prepped = req.prepare()
    print prepped.body
    print prepped.headers

    resp = s.send(prepped,timeout=5)
    print resp.status_code
    print resp.reason
    print resp.headers
    print resp.text


hard_request()