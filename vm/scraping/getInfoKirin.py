import requests
from bs4 import BeautifulSoup
import json
import codecs
# import sqlite3

# con = sqlite3.connect("/vm.sqlite3")
# cur = con.cursor()

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
    jsonArray ={}
    for i in range(tr):
        title = titles[i]
        title = title.text.replace('\u3000', ' ')

        material = materials[i]
        material = material.text

        allr = allrs[i]
        allr = allr.text

        # sql='REPLACE INTO drink (id,title,material,allr,image) VALUES (?,?,?,?,?,?);'

        jsonArray[title] = {"material":material,"allr":allr}

        # jsonData = json.dumps(jsonArray, indent=4, ensure_ascii=False)

        # data = (i,title,material,allr,'',)
        # print(jsonData)

        # cur.execute(sql,data)

        f= codecs.open('kirin.json','w','utf-8')
        json.dump(jsonArray,f, indent=4, ensure_ascii=False)

        # with open('kirin.json', 'w') as fp:
        #     json.dump(jsonArray, fp, indent=4, ensure_ascii=False)
        # con.commit()
        i += 1
    # con.close()

getInfoKirin(titles,materials,allrs)