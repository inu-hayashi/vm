import requests
from bs4 import BeautifulSoup

url = 'https://www.kirin.co.jp/products/list/nutrition/softdrink/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# titles = soup.select(".thumb")
# for title in titles:
#     print(title.text)

materials = soup.select('.explanation')
for material in materials:
    print(material.text)