#-*- coding:utf-8 -*-
import requests
"""
事件钩子：在发送请求时就注册一个事件钩子，IO请求结束后自动将response塞入回掉函数中进行回调处理
"""


def get_key_info(response,*args,**kwargs):
    """
    回调函数
    """
    print response.headers


def main():
    """
    主程序
    """
    requests.get('http://www.baidu.com', hooks=dict(response=get_key_info))

main()