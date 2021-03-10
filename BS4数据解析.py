from bs4 import BeautifulSoup
fp = open('./lagouwang.html','r',encoding='utf-8')
sp = BeautifulSoup(fp,'lxml')
print(sp.div['placeholder'])