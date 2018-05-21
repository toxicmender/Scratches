#!/usr/bin/env python3

import requests
import BeautifulSoup

def get_page(url):
    r = requests.get(url)
    content = r.content.decode('utf-8')
    return BeautifulSoup(content, 'html.parser')

def test(url):
    r = requests.get(url)
    if r.ok:
        print(r.content.decode("utf-8"))
    return r.ok

