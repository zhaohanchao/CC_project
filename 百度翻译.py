import requests
url = "https://fanyi.baidu.com/sug"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
data = {"kw":"dog"}
returnjson = requests.post(url=url,data=data,headers=UA)
print(returnjson.json())