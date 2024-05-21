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
options.add_argument('--ignore-certificate-errors')

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(300)

browser.get("https://www.lzu.edu.cn/")
#
# for i in range(107,117):
#     # browser.get("https://www.hotbox.fun/streaming")
#     html = browser.page_source
#     # # print(html)
#     # with open('.html','w',encoding='utf-8')as f:
#     #     f.write(html)
#     html = etree.HTML(html)
#     href="https://www.bilibili.com/video/BV1Yg4y127Fp/?p={}".format(i)
#
#     browser.find_element(By.XPATH, '//*[@id="mediaWebUrl"]').send_keys(href)
#     browser.find_element(By.XPATH, '//*[@id="parseButton"]').click()
#     browser.find_element(By.XPATH, '//*[@id="dlIcon4"]/a').click()
#     # browser.close()
#     browser.switch_to.window(browser.window_handles[-1])
#     # # print(html)
#     # with open('.html','w',encoding='utf-8')as f:
#     #     f.write(html)
#     html = etree.HTML(html)
#     browser.find_element(By.XPATH, '//*[@id="fileDownloadBtn0"]/span/i/span').click()
#     browser.close()
#     browser.switch_to.window(browser.window_handles[-1])
#     html = browser.page_source
#     # # print(html)
#     # with open('.html','w',encoding='utf-8')as f:
#     #     f.write(html)
#     html = etree.HTML(html)
#     browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div[2]/div/div/ul/li[1]/a/span').click()
#     browser.switch_to.window(browser.window_handles[-1])
#     print("正在下载第{}个".format(i))
#     time.sleep(5)
#
#
