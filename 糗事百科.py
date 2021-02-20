import requests
import re
import os
if not os.path.exists("./tupian"):
    os.mkdir("./tupian")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
url = 'https://www.qiushibaike.com/imgrank/'
picture_url = requests.get(url=url,headers=UA).text
# <div class="thumb">
# <a href="/article/124052554" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12405/124052554/medium/FGE8OKY8D6BG4FEW.jpg" alt="糗事#124052554" class="illustration" width="100%" height="auto">
# </a>
# </div>
pattern = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
img_list = re.findall(pattern,picture_url,re.S)
for src in img_list:

    src = 'https:' + src

    img = requests.get(url = src,headers = UA).content
    name = src.split('/')[-1]
    path = "./tupian"+"/"+name
    with open(path,'wb') as fp:
        fp.write(img)
        print("下载成功"+name)
