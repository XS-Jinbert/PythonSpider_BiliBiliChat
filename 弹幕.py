# -*- coding = utf-8 -*-
# 爬取bilibili视频弹幕
# 仅可爬1000条
# 1、查源码寻找规律
# 2、爬取网站
# 3、解析网站内容
# 4、数据保存

# import requests
import urllib.request
import urllib.error
import urllib.parse
import re
from xmltodict import parse  # 解析xml

findcid = re.compile(r'.*"cid":(.\d*),"dimension":')
findpagecid = re.compile(r'.*{"cid":(.*),"page":')

def main():
    baseurl = "https://api.bilibili.com/x/web-interface/view?bvid="
    BV = input("请输入BV号: ")
    url = baseurl + BV
    # print(url)
    getdata(url)

def getdata(url):
    getCid(url)
    pass

def savedata():
    pass

def getCid(url):
    # getCid
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.162S afari / 537.36"
    }
    request = urllib.request.Request(url, headers=head)
    cid = ""
    try:
        resqonse = urllib.request.urlopen(request)
        html = resqonse.read().decode('utf-8')
        cid = re.findall(findcid, html)[0]
        print(cid)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    # open cid to gain chatmessage
    chat = "http://api.bilibili.com/x/v1/dm/list.so?oid="+cid
    print(chat)
    try:
        # data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding='utf-8')
        # rq = urllib.request.Request(chat, data=data, headers=head, method="POST")
        # chatresqonse = urllib.request.urlopen(rq)
        # html = chatresqonse.read().decode('utf-8')
        chatresqonse = urllib.request.urlopen(chat)
        html = chatresqonse.read().decode('utf-8')
        print(html)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

if __name__ == "__main__":
    main()
