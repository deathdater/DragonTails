import fnmatch

from requests import *
from bs4 import *
import os

def homescrape():

    ALL_CHARS=[]
    all_links={}

    # avoid_links=['http://www.homeoint.org/books/boericmm/index.htm',
    #            'http://www.homeoint.org/medi-t/winbooks.htm',
    #            'http://www.homeoint.org/books/boericmm/index.htm']

    url='http://www.homeoint.org/books/boericmm/'
    # response=get(url)
    #
    # if response.status_code==200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.text)

    # small a-z characters
    for i in range(97,123):
        ALL_CHARS.append(chr(i))
    print(ALL_CHARS)
    for main in ALL_CHARS:
        visit_url=url+main+'.htm'
        response=get(visit_url)
        if response.status_code==200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all("a", href=True):
                # print(link.text)
                # # print('\t----->>\t')
                # print(link['href'])
                if link['href'] not in all_links.values():
                    all_links[link.text] = url + str(link['href'])
    medicine_dict={}


    for name,link in all_links.items():
        medicine_response=get(link)
        with open('home_links.txt', mode='a', encoding='utf-8') as f:
            f.writelines(link)
        if medicine_response.status_code == 200 :
            soup=BeautifulSoup(medicine_response.text, 'html.parser')
            title=soup.find_all('title')
            if title[0].text not in medicine_dict.keys():
                medicine_title=title[0].text
                medicine_text=soup.get_text(strip=True)
                medicine_dict[medicine_title] = medicine_text
                with open('homeo//{0}.txt'.format(medicine_title), mode='a', encoding='utf-8') as m:
                    m.write(medicine_text)
                    m.write('\n')
            # print(medicine_dict)

    print(len(medicine_dict.keys()))

    # print(len(all_links.keys())-26)


    # for x in soup.find_all("a",href=True):
    #     print(x.text)
    #     print('\t----->>\t')
    #     print(x['href'])

def homeoscrape():

    ALL_CHARS=[]
    all_links={}

    # avoid_links=['http://www.homeoint.org/books/boericmm/index.htm',
    #            'http://www.homeoint.org/medi-t/winbooks.htm',
    #            'http://www.homeoint.org/books/boericmm/index.htm']

    url='http://www.homeoint.org/allen/'
    # response=get(url)
    #
    # if response.status_code==200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.text)

    # small a-z characters
    for i in range(97,123):
        ALL_CHARS.append(chr(i))
    print(ALL_CHARS)
    for main in ALL_CHARS:
        visit_url=url+main+'.htm'
        response=get(visit_url)
        if response.status_code==200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all("a", href=True):
                # print(link.text)
                # # print('\t----->>\t')
                # print(link['href'])
                if link['href'] not in all_links.values():
                    all_links[link.text] = url + str(link['href'])
    medicine_dict={}


    for name,link in all_links.items():
        medicine_response=get(link)
        with open('home_links_allen.txt', mode='a', encoding='utf-8') as f:
            f.writelines(link)
        if medicine_response.status_code == 200 :
            soup=BeautifulSoup(medicine_response.text, 'html.parser')
            title=soup.find_all('title')
            if title[0].text not in medicine_dict.keys():
                medicine_title=title[0].text
                medicine_text=soup.get_text(strip=True)
                medicine_dict[medicine_title] = medicine_text
                with open('homeo//{0}.txt'.format(medicine_title), mode='a', encoding='utf-8') as m:
                    m.write(medicine_text)
                    m.write('\n')
            # print(medicine_dict)

    print(len(medicine_dict.keys()))

    # print(len(all_links.keys())-26)


    # for x in soup.find_all("a",href=True):
    #     print(x.text)
    #     print('\t----->>\t')
    #     print(x['href'])




def runApp():
    input_sym = ''
    count=0
    proable_medicine = []
    proable_medicine_refinded=[]
    suggested_medicine = []
    not_suggested_medicine = []
    while(input_sym!='q'):


        input_sym=input('Enter Major/Minor Symptom \n "n" to check new patient \n"q" to quit:\t\t')
        if input_sym !='q' and input_sym !='n' and  count == 0:
            for dirpath, dirs, files in os.walk('homeo'):
                for filename in fnmatch.filter(files, '*.txt'):
                    with open(os.path.join(dirpath, filename),mode='r') as f:
                        if input_sym in f.read():
                            proable_medicine.append(filename)


                            add_medicine=filename.replace(' - HOMOEOPATHIC MATERIA MEDICA - By William BOERICKE.txt','')
                            add_medicine= add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M., M.D..txt','')
                            add_medicine= add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA\nBy TIMOTHY F. ALLEN, A.M., M.D..txt','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN,\nA.M., M.D..txt','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By\nTIMOTHY F. ALLEN, A.M., M.D..txt','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F.\nALLEN, A.M., M.D..txt', '')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY\nF. ALLEN, A.M., M.D..txt','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M.,\nM.D..txt', '')
                            suggested_medicine.append(add_medicine)
                        else :
                            add_medicine = filename.replace(' - HOMOEOPATHIC MATERIA MEDICA - By William BOERICKE.txt', '')
                            add_medicine = add_medicine.replace('\n','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M., M.D..txt', '')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA\nBy TIMOTHY F. ALLEN, A.M., M.D..txt', '')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN,\nA.M., M.D..txt','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By\nTIMOTHY F. ALLEN, A.M., M.D..txt', '')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY\nF. ALLEN, A.M., M.D..txt','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F.\nALLEN, A.M., M.D..txt','')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY\nF. ALLEN, A.M., M.D..txt', '')
                            add_medicine = add_medicine.replace('. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M.,\nM.D..txt','')
                            not_suggested_medicine.append(add_medicine)

            print(suggested_medicine)
            count=count+1

            print('\n{0} number of medicines suggested.'.format(len(suggested_medicine)))
            print(count)
        elif  input_sym !='q' and input_sym !='n' and count!=0:
            suggested_medicine.clear()
            for filename in proable_medicine:
                # print(os.path.join(dirpath, filename))
                with open(os.path.join(dirpath, filename), mode='r') as f:
                    if input_sym in f.read():
                        proable_medicine_refinded.append(filename)

                        add_medicine = filename.replace(' - HOMOEOPATHIC MATERIA MEDICA - By William BOERICKE.txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA\nBy TIMOTHY F. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN,\nA.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By\nTIMOTHY F. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F.\nALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY\nF. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M.,\nM.D..txt', '')
                        suggested_medicine.append(add_medicine)
                    else:
                        add_medicine = filename.replace(' - HOMOEOPATHIC MATERIA MEDICA - By William BOERICKE.txt', '')
                        add_medicine = add_medicine.replace('\n', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA\nBy TIMOTHY F. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN,\nA.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By\nTIMOTHY F. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY\nF. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F.\nALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY\nF. ALLEN, A.M., M.D..txt', '')
                        add_medicine = add_medicine.replace(
                            '. - THE ENCYCLOPEDIA OF PURE MATERIA MEDICA By TIMOTHY F. ALLEN, A.M.,\nM.D..txt', '')
                        not_suggested_medicine.append(add_medicine)

            print(suggested_medicine)
            # count = count + 1

            print('\n{0} number of medicines suggested.'.format(len(suggested_medicine)))
            proable_medicine.clear()
            proable_medicine=proable_medicine_refinded.copy()
            proable_medicine_refinded.clear()
        else :
            count=0
            proable_medicine.clear()
            proable_medicine_refinded.clear()
            suggested_medicine.clear()







# homeoscrape()


runApp()



