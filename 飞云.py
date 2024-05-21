import hashlib
import json
import threading
import time
import redis
import pymongo
from threading import Thread
from queue import Queue
from DrissionPage import ChromiumPage, ChromiumOptions, WebPage
import ddddocr
from DrissionPage.common import Actions
import pyautogui
import pandas as pd
from datetime import datetime
import numpy
from DataRecorder import Recorder


class feishu:
    def __init__(self):
        self.redis_client = redis.Redis()
        self.client = pymongo.MongoClient()
        self.collection = self.client['飞云']['作品']
        self.collection1 = self.client['飞云']['评论']
        self.comment_queue = Queue()
        self.notice = Queue()

    def login(self):
        # co = ChromiumOptions().headless()
        page = ChromiumPage()
        # page = ChromiumPage()

        # ac = Actions(page)
        # 第一个标签页访问网址
        page.get('http://121.40.180.3:6060/', retry=3, interval=2, timeout=15)

        if page.ele('x:/html/body/div[3]/div/div/button'):
            print('已登录')

            # acess()
        else:

            for _ in range(3):
                page.ele('x:/html/body/div[1]/div/div[2]/form/div[1]/input[2]').input('13322223333')  # 输入文本
                page.ele('x:/html/body/div[1]/div/div[2]/form/div[2]/input').input('qq1133')  # 点击按钮
                imgsrc = page.ele('x:/html/body/div[1]/div/div[2]/form/div[3]/div/img').src()
                ocr = ddddocr.DdddOcr(show_ad=False)
                yzm = ocr.classification(imgsrc)
                print(yzm)
                page.ele('x://*[@id="vercode"]').input(yzm)
                page.ele('x:/html/body/div[1]/div/div[2]/form/div[5]/button').click()
                time.sleep(2)
                # page.wait.load_start()
                if '欢迎回来' not in page.ele('x:/html/body/div[1]/div/div[2]/form/div[1]/div[1]/h2').text:
                    break
                else:
                    page.refresh()
            # page.wait.load_start()  # 等待页面跳转
            print('获取到cookies', page.cookies(as_dict=True))
        self.parse(page)

    def acess(self, page, blogger, formatted_now, date_sub, date_add,formatted_one_month_ago):

        # 点击跳转
        # 用传入参数的方式执行 js 脚本显示弹出框显示 Hello world!
        #跳转进去
        redi= self.redis_client.sadd('飞书博主',blogger)
        if redi:
            page.ele('x:/html/body/div[3]/div/div/button').click()
            page.ele('x:/html/body/li[2]/div[1]/div/button[1]').click()
            # ac.move(100,200)
            #关闭这个
            page.close()
            time.sleep(3)
            #保留这个页面
            page1 = page.new_tab('http://47.96.181.102/app/#/blogger-search/index')
            # page1.run_js('alert(arguments[0]+arguments[1]);', 'Hello', ' world!')
            # time.sleep(10)
            page1.ele('x://*[@id="main-wrapper"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').click()
            # tabs = page.latest_tab
            time.sleep(2)
            #搜索页面
            page1.ele('x://*[@id="main-wrapper"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').input(blogger)
            page1.ele('x://*[@id="main-wrapper"]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/button').click()
            time.sleep(2)
            #进去博主页面

            page1.ele('x://*[@id="pane-allBlogger"]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[1]/a/button').click()

            tab = page.latest_tab

            tab.ele('x://*[@id="tab-aweme"]').click()
            # # # 监听
            tab.listen.start('weme/aweme/getawemelist?')
            data_packet_1 = tab.listen.wait()
            # print(">>>>数据包请求网址    ", data_packet_1.method, data_packet_1.url)
            url = data_packet_1.url.replace('fromDateCode={}'.format(formatted_one_month_ago), 'fromDateCode={}'.format(date_sub)).replace('toDateCode={}'.format(formatted_now),'toDateCode={}'.format(date_add)).replace('pageSize=10','pageSize=200').replace('page=1', '')
            print(url)
            page2 = page.new_tab(url)
            tab1 = page.latest_tab
            tab1.listen.start('weme/aweme/getawemelist?')
            tab1.refresh()
            data_packet = tab1.listen.wait()
            # print(">>>>数据包请求网址    ", data_packet.method, data_packet.url)
            # print(">>>>响应文本    ", data_packet.response.body, data_packet.response.raw_body)
            tab1.close()

            item = data_packet.response.body["Data"]['Items']
            for temp in item:
                shuju = {}
                shuju['博主'] = blogger
                shuju['title'] = temp["BaseAwemeDto"]["AwemeDesc"]
                shuju['时长'] = temp["BaseAwemeDto"]["DurationStr"]
                shuju['发布时间'] = temp["BaseAwemeDto"]["AwemePubTime"]
                shuju['视频销售额'] = temp['AwemeSaleCountStr']
                shuju['视频销量'] = temp["AwemeSaleGmvStr"]
                shuju['点赞'] = temp["LikeCountStr"]
                shuju['评论'] = temp["CommentCountStr"]
                shuju['分享'] = temp["ShareCountStr"]
                shuju['收藏'] = temp['CollectCountStr']
                shuju['播放量'] = temp['PlayCountStr']
                shuju['互动量'] = temp["InteractionCountStr"]
                shuju['互动率'] = temp["InteractionRateStr"]
                shuju['url'] = 'http://47.96.181.102/app/' + temp["BaseAwemeDto"]["AwemeDetailUrl"]
                shuju['抖音url'] = temp["BaseAwemeDto"]["AwemeShareUrl"]
                rediss = self.redis_client.sadd('飞书博主视频', shuju['url'])
                if rediss:
                    page3 = page.new_tab(shuju['url'])
                    tab2 = page.latest_tab
                    try:
                        shuju['平均互动率'] = tab2.ele('x://*[@id="pane-detail"]/div[2]/div[1]/div[5]/div/div/p[2]').text
                    except:
                        shuju['平均互动率'] = 0
                    try:
                        shuju['赞评比'] = tab2.ele('x://*[@id="pane-detail"]/div[2]/div[1]/div[6]/div/div/p[2]').text
                    except:
                        shuju['赞评比'] = 0


                    tab2.listen.start(['aweme/detail/segmentsPortrayal?','aweme/detail/portrayalDataV2?'])
                    tab2.ele('x://*[@id="tab-portrayal"]').click()
                    time.sleep(3)
                    tab2.ele('x://*[@id="tab-detail"]').click()
                    time.sleep(3)

                    page3.run_js('window.scrollTo(0, document.body.scrollHeight);')
                    tab2.refresh()
                    sizex, sizey = pyautogui.size()
                    print(pyautogui.size())
                    pyautogui.moveTo(sizex, sizey - 200, duration=1)
                    time.sleep(3)

                    pyautogui.click()
                    pyautogui.click()
                    pyautogui.click()
                    time.sleep(2)
                    # data_packet2s = tab2.listen.wait()
                    for data_packet in tab2.listen.steps(timeout=5):
                        print(">>>>监听的数据包url", data_packet.method, data_packet.url)
                        # print(">>>>响应文本    ", data_packet.response.body, data_packet.response.raw_body)
                        if '/portrayalDataV2?' in str(data_packet.url):
                            print('nannv')
                            # try:
                            #     temp_sex = data_packet.response.body['Data']['Gender']
                            #
                            #     shuju['男性评论比例'] = temp_sex[0]['RatioStr']
                            #     shuju['女性评论比例'] = temp_sex[1]['RatioStr']
                            # except:
                            #     shuju['男性评论比例'] = 0
                            #     shuju['女性评论比例'] = 0
                            # try:
                            #
                            #     temp_age = data_packet.response.body['Data']['Age']
                            #     try:
                            #         shuju['0-17'] = temp_age[0]['RatioStr']
                            #     except:
                            #         shuju['0-17'] = 0
                            #     try:
                            #         shuju['18-23'] = temp_age[1]['RatioStr']
                            #     except:
                            #         shuju['18-23'] = 0
                            #     try:
                            #         shuju['24-30'] = temp_age[2]['RatioStr']
                            #     except:
                            #         shuju['0-17'] = 0
                            #     try:
                            #         shuju['31-40'] = temp_age[3]['RatioStr']
                            #     except:
                            #         shuju['31-40'] = 0
                            #     try:
                            #         shuju['41-50'] = temp_age[4]['RatioStr']
                            #     except:
                            #         shuju['41-50'] = 0
                            #     try:
                            #         shuju['50+'] = temp_age[5]['RatioStr']
                            #     except:
                            #         shuju['50+'] = 0
                            # except:
                            #     print('wu')
                            #
                            #
                            #
                            #
                            #
                            # try:
                            #     temp_pro = data_packet.response.body['Data']['Province']
                            #     for k in range(0, 28):
                            #         try:
                            #
                            #             shuju[temp_pro[k]['Name']] = temp_pro[k]['RatioStr']
                            #         except:
                            #             print('暂无数据')
                            # except:
                            #     print('wu')

                        if 'segmentsPortrayal?' in str(data_packet.url):
                            print('热词')
                            # try:
                            #     temp_ci = data_packet.response.body['Data']['Segments']
                            #     for l in range(0, 10):
                            #         try:
                            #             shuju['热词{}'.format(l)] = temp_ci[l]['Name'] + temp_ci[l]['Ratio']
                            #         except:
                            #             print('re暂无数据')
                            # except:
                            #     print('wu')
                        # if 'uid=' in str(data_packet.url):
                        #     new_url=data_packet.url.replace('pageSize=10','pageSize=100000')
                        #     page5 = page.new_tab(new_url)
                        #     tab5 = page.latest_tab
                        #     tab5.listen.start('/aweme/detail/commentsv2?')
                        #     tab5.refresh()
                        #     data_packet5s= tab5.listen.steps(count=1)
                        #
                        #     # print(">>>>数据包请求网址    ", data_packet5.method, data_packet5.url)
                        #     for data_packet5 in data_packet5s:
                        #         print(">>>>数据包请求网址    ", data_packet5.method, data_packet5.url)
                        #         # print(">>>>响应文本    ", data_packet5.response.body, data_packet5.response.raw_body)
                        #         temp_comment = data_packet5.response.body['Data']['Items']
                        #         total=data_packet5.response.body['Data']['Total']
                        #
                        #         for p in range(len(temp_comment)):
                        #             comment={}
                        #             comment['视频标题']=shuju['title']
                        #             comment['博主']='余兜兜'
                        #             comment['url']=shuju['url']
                        #             comment['评论'] = temp_comment[p]['Text']
                        #             self.comment_queue.put(comment)
                        #             self.save(id=1)
                        #
                        #
                        #
                        #         tab5.close()

                page3.close()
                self.notice.put(shuju)
                self.save(id=2)
                # print(shuju)
            else:
                print('此博主已经爬')

    def save(self, id):

        if id == 1:
            item = self.comment_queue.get()
            result = True
            if result:
                self.collection1.insert_one(item)
                # self.tuwei_news(id,item["title"],item["content"],item["href"],item["time"])
                print(item)
                print('保存成功...')
                self.comment_queue.task_done()

            else:
                print('数据重复...')
                self.comment_queue.task_done()
        if id == 2:
            item = self.notice.get()
            result = True
            if result:
                self.collection.insert_one(item)
                # self.tuwei_news(id,item["title"],item["content"],item["href"],item["time"])
                print(item)
                print('保存成功...')
                self.notice.task_done()

            else:
                print('数据重复...')
                self.notice.task_done()

    # self.delete_urls_from_redis()

    @staticmethod
    def get_md5(value):
        # md5方法只能接收字节数据
        # 计算哈希值, 哈希值是唯一的, 哈希值长度为32位
        md5_hash = hashlib.md5(str(value).encode('utf-8')).hexdigest()
        return md5_hash

    def parse(self, page):
        data = pd.read_csv('./yan1.csv')
        # 获取当前时间
        now = datetime.now()

        # 格式化时间为'YYYYMMDD'形式的字符串
        formatted_now = now.strftime('%Y%m%d')
        # from datetime import datetime
        from dateutil.relativedelta import relativedelta

        # 获取当前时间
        now = datetime.now()

        # 获取当前时间的前一个月
        one_month_ago = now - relativedelta(months=1)

        # 格式化时间为'YYYYMMDD'形式的字符串
        formatted_one_month_ago = one_month_ago.strftime('%Y%m%d')



        # 遍历DataFrame中的每一行
        for index, row in data.iterrows():
            # 打印'时间节点'列的值
            date_sub = row['时间节点-20天']
            date_add = row['时间节点+20天']
            blogger = row['博主名字']
            self.acess(page, blogger, formatted_now, date_sub, date_add,formatted_one_month_ago)

    def main(self):
        self.login()


if __name__ == '__main__':
    now = time.time()
    Feishu = feishu()
    Feishu.main()
    print('任务结束: ', time.time() - now)
