import requests
from bs4 import BeautifulSoup
import sqlite3,sys,os,json,re,datetime,time

con = sqlite3.connect("../db/vm.sqlite3")
cur = con.cursor()

url = 'https://www.kirin.co.jp/products/list/nutrition/softdrink/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
titles = soup.select(".thumb")

# sql="insert into drink (id,material,allr,image,brand) VALUES (2,'title','sa','sasa','sasasa');"
#     #sqlに書いた処理を実行する
n=1
titles = soup.select(".thumb")
for title in titles:
    title = title.text
    title = title.replace('\u3000', '')

    sql='REPLACE INTO drink (id,title,material,allr,image,brand) VALUES (?,?,?,?,?,?);'

    data = (n,title,'','','','')
    # print(data)

    cur.execute(sql,data)
    # exe="'"+str(date)+"'"+(",")+"'"+str(id)+"'"+(",")+"'"+str(price)+"'"

# sql = "select * from drink";
# cur.execute(sql)
# for row in cur:
#     print(row[0], row[1])
    n += 1

con.commit()
con.close()





# ccontents = []
# for


# materials = soup.select('.explanation')
# for material in materials:
#     print(material.text)