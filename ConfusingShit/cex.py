from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

counter = 1
try:
    for i in tqdm(range(18), ascii = True, desc = "Progress"):
   
        URL = f"https://www.ebuyer.com/store/Computer/cat/Laptops?page={counter}"
        print()
        print(URL)
        print()
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        page = requests.get(URL, headers=headers)
 
        soup = BeautifulSoup(page.content, 'html.parser')
 
        for div in soup.findAll("div", {"class":"grid-item js-listing-product"}):
            price = div.find("div", {"class":"grid-item__price"})
            try:
                y =  price.div.p.text
                x = " ".join(y.split())
                print(div.h3.a.text.strip(), "-", x)
            except:
                continue
        counter += 1
except Exception as e:
    print(e)
        

