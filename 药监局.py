"http://scxk.nmpa.gov.cn:81/xk/"
import requests
import json
import time
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
main_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
ID_list = []
for i in range(5):
    i = str(i)
    main_data  = {
        'on': 'true',
        'page': i,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
        }
    json_ids = requests.post(url=main_url,data=main_data,headers=UA).json()
    for dic_id in json_ids["list"]:
        ID_list.append(dic_id['ID'])
print("get id")
time.sleep(0.2)
person_list =[]
person_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
for id_post in ID_list:
    person_data = {
        'id': id_post
    }
    person_Name = requests.post(url=person_url,data=person_data,headers=UA).json()
    person_list.append(person_Name)
fp = open("./yaojianju.json",'w',encoding='utf-8')
json.dump(person_list,fp=fp,ensure_ascii=False)
print("over")








