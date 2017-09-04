# -*- coding:utf-8 -*-
import requests

base_url = 'https://api.github.com'

def construct_url(end):
    return '/'.join([base_url,end])

def basic_auth():
    """
    基本认证
    :return:
    """
    response = requests.get(url=construct_url('user'),auth=('imoocdemo','imoocdemo123'))
    print response.headers
    print response.request.headers

def basic_oauth():
    """
    AOUTH认证
    :return:
    """
    headers = {'Authorization':'token Basic aW1vb2NkZW1vOmltb29jZGVtbzEyMw=='}
    #user/emails
    response = requests.get(construct_url(construct_url('user/emails',headers=headers)))
    print response.request.headers