#!/usr/bin/env python3

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located)
from selenium.webdriver.support.wait import WebDriverWait

def get_comment_count(driver, url):
    driver.get(url)
    class_name = 'content-banner__title'
    name = driver.find_element_by_class_name(class_name).text
    e = driver.find_element_by_id('disqus_thread')
    disqus_iframe = e.find_element_by_tag_name('iframe')
    iframe_url = disqus_iframe.get_attribute('src')
    driver.get(iframe_url)
    wait = WebDriverWait(driver, 5)

    commentCountPresent = presence_of_element_located((By.CLASS_NAME, 'comment-count'))

    wait.until(commentCountPresent)

    comment_count_span = driver.find_element_by_class_name('comment-count')
    comment_count = int(comment_count_span.text.split()[0])
    last_comment = {}
    if comment_count > 0:
        e = driver.find_elements_by_class_name('author')[-1]
        last_author = e.find_element_by_tag_name('a')
        last_author = e.get_attribute('data-username')
        if last_author != 'the_gigi':
            e = driver.find_elements_by_class_name('post-meta')
            meta = e[-1].find_element_by_tag_name('a')
            last_comment = dict(author=last_author,
                                title=meta.get_attribute('title'),
                                when=meta.text)
    return name, comment_count, last_comment
