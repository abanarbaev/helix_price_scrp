import requests, csv
from bs4 import BeautifulSoup

result = requests.get("https://helix.ru/catalog/item/40-654")

src = result.content

soup = BeautifulSoup(src, 'lxml')

urls = []

for tr_tag in soup.find_all("tr"):
    td_tag = tr_tag.find("td")
    urls.append(td_tag.attrs["href"])

print(urls)