#coding:utf-8
import requests


URL_IP = 'http://baidu.com'
URL_GET = 'https://www.baidu.com/s'


def use_simple_requests():
    response = requests.get(URL_IP)
    print response.headers
    print response.text


def use_params_requests():
    params = {'ie':'utf-8','f':'8','rsv_bp':'1','ch':'','tn':'baiduerr','bar':'','wd':'mukewang'}
    response = requests.get(url=URL_GET,params=params)
    print response.headers
   # print response.json()
    print response.status_code
    print response.reason #解释code的含义


use_simple_requests()
use_params_requests()