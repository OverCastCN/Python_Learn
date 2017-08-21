#coding:utf-8
import json
import requests

URL = r'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)#缩进为4


def request_method():
    # response = requests.get(build_uri('users/XiaoZzi'))
    # print better_print(response.text)
    response = requests.get(build_uri('user/emails'),auth = ('XiaoZzi','1250312052ai'))
    #user表示当前用户，auth添加认证
    print response.text


request_method()