# _*_ coding:utf-8 _*_
'''
Author: Laurel-rao
create time:2018/9/17 下午4:34
Remark: 
'''
import time

import requests
from selenium import webdriver

LOGIN_URL = 'https://kyfw.12306.cn/otn/login/init'

def browser():
    chrome = webdriver.Chrome()
    chrome.get(url=LOGIN_URL)
    time.sleep(100)



def test_net():

    URL = ''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    rep = requests.get(LOGIN_URL, headers=headers)

    if rep.status_code == 200:
        print(rep.text)

if __name__ == '__main__':
    browser()