import re
from requests import get
from zipfile36 import ZipFile
from .models import bhav
from bs4 import BeautifulSoup
import csv
from django.conf import settings
from equitycopy.settings import BASE_DIR
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import os
try:
    def getZip():
        cache.clear()
        if cache.get('FULLRESULT'):
            print("not cleared")
        address = "https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        res = get(address,headers=headers)
        data = BeautifulSoup(res.text,"html.parser")
        links = ''
        for link in data.find_all('a'):
            if re.match("https://www.bseindia.com/download/BhavCopy/Equity/EQ[0-9]{6}_CSV.ZIP", str(link.get('href'))):
                    links = str(link.get('href'))
                    break
        
        csvfile = links[50:58] + '.CSV'
        date = links[52:58]
        date = date[52:54] + '/' + date[54:56] + '/' + date[56:58]
        cache.set('todaydate',date)
        #cache.set('file',csvfile)
        finalres = get(links,headers=headers)
        filename = "bhavcopy.zip"
        with open(filename,"wb") as fd:
            print("extracting")
            fd.write(finalres.content)    
            fd.close()
        
        zipextractor()
        datauploader(csvfile)
except Exception as e:
    print("no worries")

def zipextractor():
    print("enter")
    fn = "bhavcopy.zip"
    with ZipFile(fn, 'r') as zip:
        print("extractibh")
        zip.extractall()
def datauploader(csvfile):
    print('1')
    add =  os.path.join(BASE_DIR, csvfile)
    file = open(add)
    csv_reader = csv.reader(file, delimiter=',')
    i=0
    for row in csv_reader:
        if i==0:
            i+=1
            continue
        newbhav = bhav()
        newbhav.code = row[0]
        newbhav.name = row[1].strip()
        newbhav.open = row[4]
        newbhav.high = row[5]
        newbhav.low = row[6]
        newbhav.close = row[7]
        newbhav.save()
        i+=1
    print("done")
    file.close()
'''    if cache.get('file'):
        oldfile = cache.get('file')
        os.remove(oldfile)'''

            

    


