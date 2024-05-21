import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://47.96.181.102/app/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
cookies = {
    "PHPSESSID": "gdug4v8hh263ftrugd9qgtpn1c",
    "body_collapsed": "0",
    "tfstk": "fHVmBi1AW-kbbTTOm7cfam45n9XJDnGsqldtXfBzq0ue0AJq78crlVDZufkaqf4_7mPqgVCiSkES35QjXffgV0axBG_X7ENuxCdActawsfhNvMCd9rax1fSd_2LYqmg_zcPRQxgYlfGN2zyun1abx0ioUtcNr_uK7f-q_q7kaqnygVRq737o50oZ_ck2a0usoI-Z_VlKAZoYckFPJV-ux_ZxD70mUYaq4IgUZqDtYrJ9KpvsoxmUu0jdiC1ZUPMg1FOiHryQf2r20icar2qn-oX95m2zJSFSKF7oMSa4LAPFfdrnilDUgYYwsrzbFb0zTNpI27mYbSDPJBDtaWHEg8B5DAhm-lPbmFAaYzULGYNGx3o_H2Grol5Fqg-9Up-j04uPW7J6CxuSrD_2nVjXhIODsabkLAMqPq1lrav6CxuSrDQlrprs34gfZ"
}
url = "http://47.96.181.102/api/v1/aweme/detail/commentsv2"
params = {
    "pageSize": "10",
    "uid": "3685151409978456",
    "awemeId": "7362423792892759323",
    "dateCode": "20240427",
    "page": "1",
    "_": "1714393005512"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
with open('comments.json', 'w', encoding='utf-8') as f:
    f.write(response.text)

print(response.text)
print(response)