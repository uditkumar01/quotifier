from re import findall
from urllib.parse import quote, quote_plus
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/quotes/tag/inspirational?page=1"
headers = {'User-Agent': 'Mozilla/5.0'}
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
z = 1
quotes = []
for section in soup.find_all(attrs={'class': 'quoteText'}):
    q = {}
    # print("*"*10)
    # print(section.contents)
    # print("*"*10)
    q["author"] = section.find(
        attrs={"class": "authorOrTitle"}).contents[0].strip().replace(',', '')
    s = str(section)
    q["quote"] = s[s.find('“')+1:s.find('”')].replace("<br/>", " ")
    quotes.append(q)
print(len(quotes))

with open("text/quotes.txt", 'w') as inputFile:
    for q in quotes:
        inputFile.write(q["quote"]+" ~ "+q["author"]+"\n")

# for i in quotes:
#     print("qoute: ",i.get("quote"))
#     print("author: ",i.get("author"))
#     print("*"*20)
