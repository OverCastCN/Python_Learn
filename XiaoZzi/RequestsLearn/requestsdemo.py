#coding:utf-8
import requests
import unittest

url_login = "https://www.signit.cn/wesign/login.html"
url_create = "https://www.signit.cn/ws-rest/v1/users/1555/envelopes"

login_views = {'username':'980850796@qq.com','password':'123456a'}
create_envelopforme = {"type":0}
# 这个部分的一定要用这样的session开头，不然后面没法保存session，就没法做认证后的操作了
s = requests.session()

response = s.post(url_login,login_views)
response = s.post(url_create,json=create_envelopforme)
result = response.json()
# 直接使用键值对提取额envelopeId
print result
print result["resultData"]["envelopeId"]

assert result["resultStatusCode"] == "100600000"
