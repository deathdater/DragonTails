# program to scrape the entries of the table
# require installation of beautifulsoup & requests

from requests import *
from bs4 import *
import logging
import http.client
http.client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
# sample table url.
url="https://www.nseindia.com/market-data/exchange-traded-funds-etf"
# "https://docs.google.com/spreadsheets/d/e/2PACX-1vSTYSqJJSjBGs6okTdvxVSNoG5laISI2GyGzfSWwyF_lY4fK4i5few7zP6q8QimhjKBBin1EuJdC3r7/pubhtml#"
# IPL 2020 url
# url='https://www.google.com/search?q=ipl+table+point+in+2020&oq=ipl+table+po&aqs=chrome.2.69i57j0i131i433i457j0i131i433j0j0i131i433j0j0i131i433l2.4609j0j7&sourceid=chrome&ie=UTF-8'
# url="https://www.iplt20.com/points-table/2020"
print(url)
number_of_columns=15
print(number_of_columns)
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
# 4
response=get(url,timeout=10.0,headers=headers)
# print(response.status_code)
page_content=response.text
# print(page_content)
soup=BeautifulSoup(page_content,'html.parser')
i = 0
# for table_row in soup.body.table.find_all('tr'):
for table_row in soup.body.find_all('tr'):
    if(len(table_row.find_all('th'))>0):
        # i = 0
        # print('\n')
        for table_header in table_row.find_all('th'):

            for header in list(table_header):
                print(header.string.replace('\n',' '), sep=' ', end='\t\t\t')

        print('\n')

    for table_data in table_row.find_all('td'):
        for data in table_data:
            if(data.string is None):
                for value in data.children:
                    if value.string is not None or value.string is not '\n':
                        print(value.string.replace('\n',' '), sep='', end='\t')
                        i+=1
            else:
                if data.string is not '\n' or data.string is not ' ':
                    i += 1
                    print(data.string.replace('\n',' '), sep=' ', end=' ')


            # else:
            #     break

        if(i%number_of_columns==0):
            print('\n')





