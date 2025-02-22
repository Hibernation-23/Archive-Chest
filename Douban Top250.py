import requests
from lxml import etree
import random
import csv

list1=['Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/129.0.0.0',
       'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/129.0.0.0',
       'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36 Edg/129.0.0.0']

head=random.choice(list1)
headers={'user-agent':head}

movie_list=[]

for page in range(1,11):

    url=f'https://movie.douban.com/top250?start={(page-1)*25}&filter='

    res=requests.get(url,headers=headers)
    
    html=etree.HTML(res.text)

    divs=html.xpath("//div[@class='info']")
    #print(divs)

    for div in divs:

        dic={}

        title=div.xpath("./div[@class='hd']/a/span[@class='title']/text()") #电影名//div[@class='info']/div[@class='hd']/a/span[1]/text()

        title_cn=''.join(title).split('\xa0/\xa0')[0]
        dic['电影中文名']=title_cn

        score=div.xpath("./div[@class='bd']/div/span[2]/text()")[0]
        dic['评分']=score

        #print(title_cn,score)

        #print(len(movie_list))
        movie_list.append(dic)

with open('豆瓣Top250.csv','w',encoding='utf-8-sig',newline='') as f:

    writer=csv.DictWriter(f,fieldnames=('电影中文名','评分'))

    writer.writeheader()

    writer.writerows(movie_list)


#xpath的使用
#title=html.xpath('//div[@class="hd"]/a/span[1]/text()') #电影名

##score=html.xpath('//div[@class="star"]/span/text()') #评分
##score=html.xpath('//div[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[2]/div/span[2]') #评分
#score=html.xpath("//div[@class='info']/div[@class='bd']/div[@class='star']/span[2]/text()") #评分



