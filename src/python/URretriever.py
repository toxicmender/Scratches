#!/usr/bin/env python3

import urllib

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data, headers)

try:
    response =  urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error Code: ', e.code)
except urllib.error.URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    the_page = response.read()
