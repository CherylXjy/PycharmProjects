# -*- coding: utf-8 -*-

#document object model

import bs4, re
print bs4

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(
                    html_doc,               # HTML文档字符串
                    'html.parser',           # HTML解析器
                    from_encoding='utf-8'    # HTML文档的编码
                    )

#搜索节点
#查找所有标签为a
#soup.find_all('a')
#soup.find_all('a', href='/view/123.htm')
#soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
#soup.find_all('div', class_='abc', string='Python')


#得到节点: <a href='1.html'>Python</a>
#获取查找到的节点的标签名称
#node.name
#获取查找到的a节点的href属性
#node['href']
#获取节点的链接文字
#node.get_text()

links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print
link_node = soup.find('a', href='http://example.com/lacie')
print link_node.name, link_node['href'], link_node.get_text()

print
link_node = soup.find('a', href=re.compile(r"ill"))
print link_node.name, link_node['href'], link_node.get_text()

print
link_node = soup.find('p', class_='title')
print link_node.name, link_node.get_text()