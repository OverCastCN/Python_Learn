#coding:utf-8
import json
import requests
from requests import exceptions

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout = 10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print response.text

timeout_request()