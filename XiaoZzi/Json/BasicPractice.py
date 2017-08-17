#coding:utf-8
import urllib2
import json

# html = urllib2.urlopen(r'')
#
# hjson = json.loads(html.read())
#
# print hjson['envelopeId']

a = {"resultStatusCode":"100600000","resultCode":0,"resultDesc":"信封操作成功","resultData":{"envelopeId":"dbab3338-fbd8-46c9-be7c-def75969382f","link":{"href":"/ws-rest/v1/users/1831/envelopes/dbab3338-fbd8-46c9-be7c-def75969382f","method":"GET"},"statusDatetime":1502866352000,"type":0,"status":0}}
print a['resultData']['envelopeId']

b = {
    "resultData": {
        "recipients": [
            {
                "recipientId": 158730,
                "contact": "1101066076@qq.com",
                "name": "杨州",
                "sequence": 1
            },
            {
                "recipientId": 158731,
                "contact": "1518778189@qq.com",
                "name": "杨州",
                "sequence": 1
            }
        ]
    },
    "resultCode": 0,
    "resultDesc": "信封操作成功",
    "resultStatusCode": "100600000"
}

print b["resultData"]["recipients"][0]["recipientId"]

