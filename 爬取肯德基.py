import requests
import json
url  = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
data  ={
    'cname':  '',
    'pid': '',
    'keyword': '泰安',
    'pageIndex': '1',
    'pageSize': '10',
}
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
response  = requests.post(url=url,data = data,headers=UA)


with open("./KFC.text",'w',encoding='utf-8') as fp:
    fp.write(response.text)
    print("爬取成功")


