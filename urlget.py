#!/usr/bin/python3

import re
import sys
from bs4 import BeautifulSoup as bs
import urllib.parse
import urllib.request


regex = r'('
# Scheme (HTTP, HTTPS, FTP and SFTP):
regex += r'(?:(https?|s?ftp):\/\/)?'
# www:
regex += r'(?:www\.)?'
regex += r'('
# Host and domain (including ccSLD):
regex += r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+)'
# TLD:
regex += r'([A-Z]{2,6})'
# IP Address:
regex += r'|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
regex += r')'
# Port:
regex += r'(?::(\d{1,5}))?'
# Query path:
regex += r'(?:(\/\S+)*)'
regex += r')'

rx_url = re.compile(regex, re.IGNORECASE)


def get_url(string):
    #  url = find_urls_in_string.search(string)
    #  return url
    return rx_url.search(string).group()


try:
    url = sys.argv[1]
except:
    url = 'http://google.com'


me = {'name': 'Emil Zaterov',
      'location': 'Liverpool',
      'language': 'Python3'}

data = urllib.parse.urlencode(me)
data = data.encode('ascii')
#req = urllib.request.Request(url, data)
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as r:
    page = r.read()

soup = bs(page)
#  soup = bs(sys.argv[1])

links = []
for line in soup.find_all("a"):
    print(line)
    link = line.get('href')

    try:
        if link.startswith('http'):
            links.append(get_url(link))
    except:
        pass


# python2
# print '\n'.join(str(l) for l in links)
print(*links, sep='\n')



'''
BAI
http://stream.wbai.org:8000/wbai_128:

<audio controls style="margin-top:0px;width:250px;opacity:0.66;"><source src="http://stream.wbai.org:8000/wbai_128"></source></audio> 

WWOZ
http://wwoz-sc.streamguys.com:80/wwoz-hi.mp3:
<div


