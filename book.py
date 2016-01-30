# -*- coding: utf-8 -*-
# 豆瓣图书搜素功能的实现
import urllib2,json

def query_book(word):
    qword = urllib2.quote(word)
    bookurlbase = r"https://api.douban.com/v2/book/search?q=" 
    url = bookurlbase+qword
    searchresult = urllib2.urlopen(url).read() 
    bookid = json.loads(searchresult)['books'][0]['id']
    doubanapi = r"https://api.douban.com/v2/book/"    
    bookurl = doubanapi + bookid
    injson = urllib2.urlopen(bookurl).read()
    book  =  json.loads(injson)	
    return book