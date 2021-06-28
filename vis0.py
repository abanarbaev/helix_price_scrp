import requests
from bs4 import BeautifulSoup

result =  requests.get("https://helix.ru/catalog")

print(result.status_code)

#print(result.headers)

src = result.content
#print(src)

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all('a')
print(links)
print("\n")

for link in links:
    if "Каталог" in link.text:
        print(link)
        print(link.attrs["href"])


