from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup
import requests

counter = 1

try:
   
    URL = "https://uk.webuy.com/search?inStock=1&categoryIds=892&view=list&inStockOnline=1"
    print()
    print(URL)
    print()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    page = requests.get(URL, headers=headers)
 
    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup)

    for div in soup.findAll("div", {"class":"mainPageArea"}):
            desc = div.find("div", {"class":"desc"})
            print(desc.h.a.text)
            
except Exception as e:
    print(e)
