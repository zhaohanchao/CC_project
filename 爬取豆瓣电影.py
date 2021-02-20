import requests
import json
url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0&genres=%E5%96%9C%E5%89%A7"
data = {
    'sort': 'U',
    'range': '0,10',
    'tags':'' ,
    'start': '0',
    'genres': '喜剧'
}
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
response  = requests.get(url=url,headers=UA)
dec_return = response.json()
fp = open("./douban.json",'w',encoding='utf-8')
json.dump(dec_return,fp=fp,ensure_ascii=False)




