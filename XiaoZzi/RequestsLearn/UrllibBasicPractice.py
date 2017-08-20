#coding:utf-8
import urllib
import urllib2


URL_IP = 'http://baidu.com'
URL_GET = 'https://www.baidu.com/s'#?ie=utf-8&f=8&rsv_bp=1&ch=&tn=baiduerr&bar=&wd=mukewan'

#不带参数的链接
def use_simple_urllib2():
    responce = urllib2.urlopen(URL_IP)
    print 'Header:'
    print responce.info()  #get headers
    print 'Body:'
    print ''.join([line for line in responce.readlines()])

#带参数的链接
def use_params_urllib2():
    #构建请求参数
    params = urllib.urlencode({'ie':'utf-8','f':'8','rsv_bp':'1','ch':'','tn':'baiduerr','bar':'','wd':'mukewang'})
    print 'Request Params:' + params
    response = urllib2.urlopen('?'.join([URL_GET,'%s']) % params)
    print 'Header:'
    print response.info()
    print 'Code:'
    print response.getcode()
    print 'Body:'
    print ''.join([line for line in response.readlines()])

use_simple_urllib2()
use_params_urllib2()

print '?'.join(['2','%s']) % '2'