#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def get_page(url):
    r = requests.get(url)
    content = r.content.decode('utf-8')
    return BeautifulSoup(content, 'html.parser')

def get_page_articles(page):
    elements = page.findAll('article')
    articles = [e.a.attrs['href'] for e in elements]
    return articles

page = get_page('https://tutsplus.com/authors/gigi-sayfan')
articles = get_page_articles(page)
prefix = 'https://code.tutsplus.com/tutorials'
for a in articles:
    print(a[len(prefix):])
