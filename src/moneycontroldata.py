from requests import *
from bs4 import *
import json
import logging
import http.client
# http.client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

url="https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT"

headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}


def getStockLinks():
    stock_list_url='https://www.moneycontrol.com/india/stockpricequote/'
    ALL_CHARS = []
    all_links = {}

    for i in range(65, 91):
        ALL_CHARS.append(chr(i))
    ALL_CHARS.append('others')
    # print(ALL_CHARS)
    for link in ALL_CHARS:
        visit_url=stock_list_url+link
        response = get(visit_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            list_of_tabledata_norm=soup.find_all("a", attrs={"class":"bl_12"})
            # list_of_tabledata_last = soup.find_all("a", attrs={"class": "last"})
            # print(len(list_of_tabledata_norm))

            for stock in list_of_tabledata_norm :
                if(len(stock.get_text())>0):
                    all_links[stock.get_text()]=stock.get('href')
                # if stock.contents[0].has_attr('href'):
                #     print(stock.get('href'))


                # print(stock.find_all("a",href=True))
    return all_links


def get_scIdList(_url):
    try:
        response=get(_url,timeout=10.0,headers=headers)
        page_content=response.text

        soup=BeautifulSoup(page_content,'html.parser')
        scidlist_tag=soup.find(name="input",attrs={"type":"hidden","id":"scIdList"})
        print('\n')
        if(scidlist_tag is not None):
            scidlist=scidlist_tag.get('value')
            print(scidlist)
            return scidlist.split(",")
        else:
            return "error"
    except:
        print('request timeout')
        return "error"


def getMoneyControlDetail(stock_id):

    url='https://priceapi.moneycontrol.com/pricefeed/nse/equitycash/'
    try:
        response=get(url+stock_id,timeout=5,headers=headers)
        if(response.status_code==200):
            print("Success")
            # print(response.json())
            return response.json()
        else:
            print("Error Occurred")
            return None
    except:
        return None


def writeStockDataFile_moneyControl(dict_data_obj):

    with open("StockData//{0}.json".format(dict_data_obj['company']), "w",encoding='utf-8') as outfile:
        outfile.write(json.dumps(dict_data_obj,indent=4))



def dataSetup():
    all_stocks_links=getStockLinks()
    for stock,link in all_stocks_links.items():
        print(stock)
        scIdList=get_scIdList(link)
        print(scIdList[0])
        stock_details = getMoneyControlDetail(scIdList[0])


        if stock_details!=None and scIdList!="error":
            stock_info_json = stock_details['data']
            print(stock_info_json)
            if stock_info_json!=None:
                data_dict=dict(stock_info_json)
                data_dict['stock']=link
                data_dict['moneyControlLink'] = stock
                data_dict['scIdList'] = scIdList
                # final_data=json.dumps(data_dict)
                print(data_dict)
                writeStockDataFile_moneyControl(data_dict)

dataSetup()