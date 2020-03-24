import requests
from bs4 import BeautifulSoup
import sqlite3,sys,os,json,re,datetime,time

con = sqlite3.connect("../db/vm.sqlite3")
cur = con.cursor()

url = 'https://www.kirin.co.jp/products/list/nutrition/softdrink/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml',from_encoding='utf-8')
titles = soup.select(".thumb")
materials = soup.select('.explanation')


tr = soup.select(".nutrition  .thumb")
tr = len(tr)

def getInfoKirin(titles,materials):
    for i in range(tr):
        n=1
        for title in titles:
            title = title.text
            title = title.replace('\u3000', '')

        for material in materials:
            material = material.text
            material = material.replace('\u3000', '')

    # titles = soup.select(".thumb")
    # for title in titles:
    #     title = title.text
    #     title = title.replace('\u3000', '')

        sql='REPLACE INTO drink (id,title,material,allr,image,brand) VALUES (?,?,?,?,?,?);'

        data = (n,title,material,'','','')
        print(data)

        cur.execute(sql,data)

        n += 1


        i += 1
    con.commit()
    con.close()

getInfoKirin(titles,materials)





# ccontents = []
# for


# materials = soup.select('.explanation')
# for material in materials:
#     print(material.text)