#!usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

with open('./web/new_index.html', 'r') as wbData:
    Soup = BeautifulSoup(wbData, 'lxml')

    #选取某一个元素
    #images = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > img')

    #去掉具体的位置信息后,选取某一类信息
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info > span')

#    print(images, titles, descs, rates, cates, sep='\n---------------------\n')


for title, image, desc, rate, cate in zip(titles, images, descs, rates, cates):
    data = {
        'title':title.get_text(),
        'rate':rate.get_text(),
        'desc':descs.get_text(),
        'cate':cates.get_text(),
        'image':image.get('src')
    }
    print(data)







    '''
    body > div.main-content > ul > li:nth-child(1) > img
    body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
    body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
    body > div.main-content > ul > li:nth-child(1) > div.rate > span
    body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(1)
    '''
