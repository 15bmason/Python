from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup
import requests
 
 
 
URL = 'https://www.argos.co.uk/browse/technology/laptops-and-pcs/laptops-and-netbooks/c:30049/'
 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
page = requests.get(URL, headers=headers)
 
soup = BeautifulSoup(page.content, 'html.parser')
 
for div in soup.findAll('div', attrs={'class': 'ProductCardstyles__TextContainer-l8f8q8-6 fDOdUb'}):
    print(div.text.strip())

next_page = soup.find("div", {"class": "next-container"})

if next_page:
    next_url = next_page.find("a", href=True)

    if next_url:
        root_url = next_url['href']


print(next_url)
