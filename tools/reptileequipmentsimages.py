# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: reptile equipments images from official website
# Created: 2024.01.05
# History:
# <version>    <time>        <desc>
# v0.1      2024/01/05    basic build success
# -----------------------------


import json
import re
import requests
from bs4 import BeautifulSoup, element
from urllib.parse import urljoin

import os


# 抓取网页
def get_html(url: str):
    response = requests.get(url)
    
    print(f'<Response: {response.status_code} >')

    return response.content.decode('gbk') 

def data_process(url: str, html: str, output: str):
    global statistic
    items_json = open(os.path.join(output, 'items.json'), 'a', encoding='utf-8')  # auto create

    html_soup = BeautifulSoup(html, 'lxml')

    if statistic[0] % 1000 < 15 and statistic[0] % 1000 != 12:
        eqs = html_soup.find_all('tbody')[1].find_all('tr')[1: 8]
    elif statistic[0] % 1000 == 12:
        eqs = html_soup.find_all('tbody')[2].find_all('tr')[1: 8]
    else:
        eqs = html_soup.find_all('tbody')[1].find_all('tr')[2: 9]
    # save images and insert info into json1
    for eq in eqs:
        infos = eq.find_all('td')

        ima_path = urljoin(url, infos[0].find('img')['src'])
        ima = requests.get(ima_path).content

        eq_name = infos[1].text.strip('\n')
        eq_level = infos[3].text.strip('\n')

        statistic[int(eq_level) // 10 - 1] += 1  # curr id
        eq_json = {
            'ID': eq_level + str(statistic[int(eq_level) // 10 - 1]).zfill(2),
            'NAME': eq_name,
            'LEVEL': eq_level, 
            'VALUE': 0,
        }
        print(eq_json)
        with open(os.path.join(output, eq_json['ID'] + '.png'), 'wb') as ifile:
            ifile.write(ima)
        items_json.write(json.dumps(eq_json, ensure_ascii=False) + '\n')
    

if __name__ == "__main__":
    urls = ['https://xyq.163.com/introduce/dj004.html',
            'https://xyq.163.com/dj004_2.html',
            'https://xyq.163.com/dj004_3.html',
            'https://xyq.163.com/dj004_4.html',
            'https://xyq.163.com/dj004_5.html',
            'https://xyq.163.com/dj004_6.html',
            'https://xyq.163.com/dj004_7.html',
            'https://xyq.163.com/dj004_8.html',
            'https://xyq.163.com/dj004_9.html',
            'https://xyq.163.com/dj004_10.html',
            'https://xyq.163.com/dj004_11.html',
            'https://xyq.163.com/dj004_12.html',
            'https://xyq.163.com/dj004_13.html',
            'https://xyq.163.com/dj004_14.html',
            'https://xyq.163.com/dj004_15.html',
            'https://xyq.163.com/dj004_16.html',
            'https://xyq.163.com/dj004_17.html',
            'https://xyq.163.com/dj004_18.html',
            'https://xyq.163.com/dj004_19.html',]
    
    output = "./resources/items"
    statistic = [0] * 7
    
    for url in urls:
        html = get_html(url)
        data = data_process(url, html, output)