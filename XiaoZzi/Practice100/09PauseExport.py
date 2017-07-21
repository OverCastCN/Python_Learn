# -*- coding:utf-8 -*-
"""
暂停三秒输出
"""

import time
a = {1:2,3:4}
for k,v in a.items():
    print k,v
    time.sleep(3)