import urllib2

#1
response = urllib2.urlopen("www.baidu.com")

#获取状态码
print response.getcode()

#读取内容
cont = response.read()


#2
request = urllib2.Request(url='')
request.add_data('a', '1')
request.add_header('User-Agent', 'Mozilla/5.0')
response = urllib2.urlopen(request)

#3
import cookielib
#创建cookie容器
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
#使用带有cookie的urllib2访问网页
response = urllib2.urlopen('http://www.baidu.com/')




