# -*- coding:utf-8 -*-
"""
暂停三秒输出并格式化当前时间
"""
import time
print time.localtime(time.time())
time.sleep(3)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))