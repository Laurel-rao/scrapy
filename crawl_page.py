# _*_ coding:utf-8 _*_
'''
Author: Laurel-rao
create time:2018/9/17 下午4:34
Remark: 
'''
import re
from time import sleep


from http import cookiejar
from urllib import request
from urllib import parse
import requests
import json
from selenium import webdriver

LOGIN_URL = 'https://kyfw.12306.cn/otn/login/init'
buy_ticket = 'https://kyfw.12306.cn/otn/leftTicket/init'

def browser(locations='深圳北', destination='南昌西'):
    chrome = webdriver.Chrome()
    chrome.get(url=LOGIN_URL)
    chrome.find_element_by_id('username').send_keys('1562766937@qq.com')
    chrome.find_element_by_id('password').send_keys('zxcv19961125')

    while True:
        # 判断是否登陆成功
        if re.findall('index', chrome.current_url):
            break
    cookies = chrome.get_cookies()
    with open('sign.json', 'w') as ff:
        ff.write(json.dumps(cookies))
    chrome.find_element_by_css_selector('#selectYuding>a').click()
    # chrome.find_element_by_id('fromStationText').click()
    chrome.find_element_by_id('fromStationText').send_keys(locations)
    # chrome.find_element_by_css_selector('.citylineover .ralign').send_keys(destination)

    chrome.find_element_by_id('toStationText').click()
    chrome.find_element_by_id('toStationText').send_keys(destination)

    chrome.find_element_by_css_selector('input.inp_selected').click()




class view_train():
    def __init__(self):
        self.chrome = webdriver.Chrome()
        # self.request =

    def login(self, filename='sign.json'):
        with open(filename) as ff:
            cookies = json.loads(ff.read())
        self.chrome.get(buy_ticket)
        for cookie in cookies:
            self.chrome.add_cookie({
                'name': cookie['name'],
                'value': cookie['value'],
                'path': True,
            })
        self.chrome.get(buy_ticket)

    def stay_forever(self):
        while True:
            pass


if __name__ == '__main__':
    a = view_train()
    a.login()
    a.stay_forever()