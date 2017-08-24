# -*- coding:utf-8 -*-
import requests


def download_image():
    """
    demo:下载图片，文件
    :return:
    """
    headers = {}
    #伪造headers信息
    url = 'http://img3.imgtn.bdimg.com/it/u=2394543825,2451299386&fm=26&gp=0.jpg'
    #图片格式无法直接使用content打印。需要使用stream，让文件用比特流的方式过来
    response = requests.get(url=url,headers=headers,stream = True)
    #然后读取这个比特流，将其转存到本地文件
    with open('demo.jpg','wb') as fd:
        #用二进制只读的方式打开demo.jpg的文件
        for chunk in response.iter_content(128):
            #遍历所有内容，每128个字节写入一次
            fd.write(chunk)
    print response.status_code,response.reason
    print response.headers

download_image()


def download_image_improved():
    """
    demo:下载图片,使用之后关闭流
    :return:
    """
    headers = {}
    url = 'http://img3.imgtn.bdimg.com/it/u=2394543825,2451299386&fm=26&gp=0.jpg'
    response = requests.get(url=url, headers=headers, stream=True)
    #contextlib专门管理上下文信息
    from contextlib import closing
    #读取完这个比特流之后将其关闭掉
    with closing(requests.get(url=url, headers=headers, stream=True)) as response:
        with open('demo.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)
