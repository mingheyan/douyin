from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from urllib import request
import sys
from datetime import datetime


 # 创建浏览器配置对象
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 屏蔽开发者警告
options.add_argument(r"user-data-dir=C:\Users\yan\AppData\Local\Google\Chrome\User Data")  # 浏览器路径
# 屏蔽图片
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option('prefs', prefs)
# #防止自动退出
options.add_experimental_option("detach",True)
#无头模式

# options.add_argument('--headless')

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(20)

browser.get("http://121.40.180.3:6060/web/index")


html = browser.page_source
# # print(html)
# with open('.html','w',encoding='utf-8')as f:
#     f.write(html)
html = etree.HTML(html)
# 点击二维码
browser.find_element(By.XPATH, '/html/body/div[3]/div/div/button').click()
ifram = browser.find_element(By.XPATH, '//*[@id="layui-layer-iframe1"]')
browser.switch_to.frame(ifram)
browser.find_element(By.XPATH, '/html/body/li[2]/div[1]/div/button[1]').click()
browser.switch_to.window(browser.window_handles[-1])
browser.get('http://47.96.181.102/app/#/blogger-search/index')
browser.switch_to.window(browser.window_handles[-1])
html = browser.page_source
# # print(html)
# with open('.html','w',encoding='utf-8')as f:
#     f.write(html)
html = etree.HTML(html)
browser.find_element(By.XPATH, '//*[@id="main-wrapper"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').send_keys('mao0858288')
browser.find_element(By.XPATH,'//*[@id="main-wrapper"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/button').click()
browser.switch_to.window(browser.window_handles[-1])
browser.find_element(By.XPATH,'//*[@id="pane-allBlogger"]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/img').click()
browser.switch_to.window(browser.window_handles[-1])
html = browser.page_source
# # print(html)
# with open('.html','w',encoding='utf-8')as f:
#     f.write(html)
html = etree.HTML(html)
browser.find_element(By.XPATH,'//*[@id="tab-aweme"]').click()



print('正在打开')
