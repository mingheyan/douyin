import time

import requests
import json




headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://47.96.181.102/app/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
cookies = {
    "UM_distinctid": "18f2e14b1a7ff9-0f58a34a632fd4-26001d51-190140-18f2e14b1a81a91",
    "PHPSESSID": "iuk3lfsik0ksnrjjprlpsqpbi7",
    "body_collapsed": "0",
    "CNZZDATA1281116375": "197854868-1714465059-null%7C1714982053",
    "tfstk": "f97jLhcbRxDbU4fWInFyPOmXCc8_ctaekfOOt1h9HEptegO2ThdxWnIWyCAwHSYw7T9WeO8w3Z7q5hpPpiuamiP1FtWP7iuN5g01t1b4iFPDosYMWJyU8F1ciF2Oj1EFlQhJT_3tkVekqU-HWJyUzgUgor8ObABCJU1JEIixkOnYyLpkTAL9HhH-2BpJBFLOBU3JgCHtHIKty0hKMzOz_K1bQzBXUxh9aspSRb7WMpicGLgtWagecpeeFV3OPI1koIpnRlJdxK-eETUrlF1J19OChYeWW__cR3QYEV125K6XZg2sfpsOgMj9VSUANE9XAa6u88YfXtb6miGgt_LAEMvHDu2kNZ7efpxSe-CPNKKCftyoWKSCwTtFzYuey6IWPgSx8p_PcclWxVOWL7NSjc-54AXr8ii0bndkavP7NxTJDQAWL7NSjcxvZQPUN7MXy"
}
url = "http://47.96.181.102/api/v3/blogger/aweme/aweme/getawemelist"
params = {
    "uid": "3685151409978456",
    "searchtype": "1",
    "keyword": "",
    "fromDateCode": "20240406",
    "toDateCode": "20240506",
    "isNotDelete": "false",
    "sort": "PubTime",
    "order": "1",
    "page": "1",
    "pageSize": "20",
    "_": "1714982056223"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
with open('vedio.json', 'w', encoding='utf-8') as f:
    f.write(response.text)
item=json.loads(response.text)
#总共
total=item['Data']['Total']
#每一个
for temp in item['Data']['Items']:
    print(item)
    time.sleep(2)

    item=temp['BaseAwemeDto']
    #awemeId
    awemeId =item['AwemeId']
    #title
    AwemeDesc = item['AwemeDesc']
    #time

    AwemePubTime = item['AwemePubTime']
    #视频链接
    AwemeDetailUrl = item['AwemeDetailUrl']
    #抖音链接
    AwemeShareUrl = item['AwemeShareUrl']
    #时长
    DurationStr = item['DurationStr']
    #视频销售额
    AwemeSaleCountStr = temp['AwemeSaleCountStr']
    #视频销量
    AwemeSaleGmvStr = temp['AwemeSaleGmvStr']
    #点赞量


    print(AwemeSaleCountStr)
    print(awemeId,AwemeDesc,AwemeDetailUrl,AwemeShareUrl)





# print(response.text)
print(response)