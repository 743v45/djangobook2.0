#coding:utf-8
import urllib
import urllib2
import re

def download(suffix, page):
    url = 'http://djangobook.py3k.cn/2.0/'
    url = url + suffix
    file = open(suffix[0:-1],'w')
    file.write(page)
    file.close()

def run():
    url = 'http://djangobook.py3k.cn/2.0/'
    user_agent ='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    values = {'name' : 'Michael Foord',
        'location' : 'Northampton',
        'language' : 'Python' 
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url,data,headers)
    response = urllib2.urlopen(req)
    the_page = response.read()
    #print the_page
    file = open('django.html','w')
    file.write(the_page)
    file.close()
    p = re.compile('<a href="(.*?)">阅读</a>')
    sites = p.findall(the_page)
    print sites
    for site in sites:
        req = urllib2.Request(url+site,data,headers)
        response = urllib2.urlopen(req)
        page = response.read()
        download(site,page)

if __name__ == '__main__':
    run()
