participaciones=5

import requests
from bs4 import BeautifulSoup

url='https://app.tikr.com/stock/multiples?cid=4773318&tid=154175737&tab=multi&ref=9julwp'
response= requests.get(url)

if response.status_code==200:
    html= response.text
    soup=BeautifulSoup(response.content,'html.parser')
    tags=soup.find_all('td',attrs={'class':'text-right black--text'})

    for tag in tags:
        print(tag.get_text())
        
else:
    print('Error al obtener la página:', response.status_code)

