# program to scrape the entries of the table
# require installation of beautifulsoup & requests

from requests import *
from bs4 import *

# sample table url.
url="https://docs.google.com/spreadsheets/d/e/2PACX-1vSTYSqJJSjBGs6okTdvxVSNoG5laISI2GyGzfSWwyF_lY4fK4i5few7zP6q8QimhjKBBin1EuJdC3r7/pubhtml#"
number_of_columns=4
response=get(url)
page_content=response.text
soup=BeautifulSoup(page_content,'html.parser')
i = 0
for table_row in soup.body.table.find_all('tr'):
    for table_data in table_row.find_all('td'):
        for data in list(table_data):
            # if('Computational'in data.string):
            print(data.string, sep='  ', end='\t\t')
            i += 1
            # else:
            #     break

            if(i%number_of_columns==0):
                print('\n\n')





