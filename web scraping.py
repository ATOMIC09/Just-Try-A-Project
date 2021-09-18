import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/th/"
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text, 'html.parser')
find_word = soup.find_all("table",{"class":"cmc-table.cmc-table___11lFC.cmc-table-homepage___2_guh "})

for i in find_word:
    print(i)