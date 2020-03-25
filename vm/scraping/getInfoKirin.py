import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect("/vm.sqlite3")
cur = con.cursor()

url = 'https://www.kirin.co.jp/products/list/nutrition/softdrink/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml',from_encoding='utf-8')
titles = soup.select(".thumb")
materials = soup.select('.explanation')
allrs = soup.select('.nutrition tr')
allrs = soup.select('.nutrition td:nth-of-type(3)')

tr = soup.select(".nutrition  .thumb")
tr = len(tr)


def getInfoKirin(titles,materials,allrs):
    for i in range(tr):
        title = titles[i]
        title = title.text.replace('\u3000', ' ')

        material = materials[i]
        material = material.text

        allr = allrs[i]
        allr = allr.text


    # titles = soup.select(".thumb")
    # for title in titles:
    #     title = title.text
    #     title = title.replace('\u3000', '')

        sql='REPLACE INTO drink (id,title,material,allr,image) VALUES (?,?,?,?,?,?);'

        data = (i,title,material,allr,'',)
        print(data)

        cur.execute(sql,data)

        i += 1
    con.commit()
    con.close()

getInfoKirin(titles,materials,allrs)





# ccontents = []
# for


# materials = soup.select('.explanation')
# for material in materials:
#     print(material.text)