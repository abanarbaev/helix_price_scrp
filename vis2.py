from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Pirate vBay</title></head>
<body>
<p class="title"><b>ThePirate vBay</b></p>
<p class="story">Once Upon a time theree was ThePirate vBay...; th was sisters, their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link1">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link1">Tillie</a>;
and they lived at the bpttpm of a well.</p>
<p class="story">...</p>
<b class=boldest">Extremly bold</b>
<blockquote_class="boldest">Extremly bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, "lxml")

#print(soup.prettify())

#print(soup.b)

#print(soup.find("b"))

#print(soup.find_all("b"))

#print(soup.b.name)

#tag = soup.b
#print(tag)
#tag.name = "blockquote"
#print(tag)

#tag = soup.find_all("b")[2]
#print(tag)
#print(tag['id'])

#tag = soup.find_all('b')[3]
#print(tag)
#print(tag['id'])
#print(tag['another-attribute'])


#tag = soup.find_all('b')[3]
#print(tag)

#print(tag.attrs)

#print(tag)
#tag['another-attribute'] = 2
#print(tag)

#del tag['id']
#del tag['another-attribute']
#print(tag)

#tag = soup.find_all('b')[3]
#print(tag)
#print(tag.string)

#tag.string.replace_with('This is another string')
#print(tag)