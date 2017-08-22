#coding:utf-8
import json
import requests


"""
第一种URL参数提交，典型为淘宝
http://list.tmall.com/
search_product.htm?cat=5051..
params:request.get(url,params={'key1':'value1','key2':'value2'})
"""
# URL = 'https://pages.tmall.com/wow/act/15879/phonebazaareins'


# params = {'spm':'875.7931836/B.2016006.d1.5fda28c6ffL7sT','trackInfo':'20160815100101;9263605563;95983;540069226936;3;95983_540069226936;1007.14152.68669.100200300000000;e1f3acdc-62b0-49e0-906c-7d5aa6771e85;1;0;10000002','item_id':'540069226936','pvid':'e1f3acdc-62b0-49e0-906c-7d5aa6771e85','pos':'1','activity_id':'95983','acm':'07055.1003.1.1192426','scm':'1003.1.20160815.OTHER_0_2019220'}


# response = requests.get(URL,params=params)
# print response.text


"""
第二种表单参数提交，常见论文提交
Content-Type:application/x-www-form-urlencoded
内容：key1=value1&key2=value2
requests.post(url,data={'key1':'value1','key2':'value2'})
"""


"""
第三种：json参数提交：
Content-Type:application/x-www-form-urlencoded
内容：key1=value1&key2=value2
requests.post(url,data={'key1':'value1','key2':'value2'})
"""

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL,endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)


def params_method():
    response = requests.get(build_uri('users'),params={'since':11})
    print better_print(response.text)
    print response.request.headers
    print response.url


def json_request():
    # response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'), json ={'name':'babymooc2','email': '9808507@qq.com'})
    #修改邮箱
    response = requests.post(build_uri('user/emails'),auth = ('imoocdemo', 'imoocdemo123'),json=['helloworld@imooc.com'])
    #增加邮箱
    # response = requests.delete(build_uri('user/emails'),auth = ('imoocdemo', 'imoocdemo123'))
    #去除邮箱
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code
    print response.reason

# params_method()
json_request()