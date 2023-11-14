from requests import *
from bs4 import *
import os
url='https://jamcircuit.com/find/?pg=257&sort=nearby'
# url='https://jamcircuit.com/find/?sort=nearby'
# for i in range(2):
newurl = url.format(1)
response=get(url)
if response.status_code==200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    main_desc = soup.body.find_all('div', class_='lf-item-info-2')
    print(main_desc)
    city_names = soup.body.find_all('div', class_='lf-head')
    print(city_names)
    category_names = soup.body.find_all('span', class_='category-name')
    print(category_names)
else:
    print (response.status_code)
for k in range(len(main_desc)):
    print(main_desc[k].text+'\t'+city_names[k].text+'\t'+category_names[k].text)