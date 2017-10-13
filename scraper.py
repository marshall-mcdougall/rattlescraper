#this file contains all the functions concerned with scraping
#html table sites
#google map sites
#get data
#misc scraper

import requests
import json
from bs4 import BeautifulSoup
from bin.py import Bin


#Salvation Army Thrift Store
url1 = "https://www.thriftstore.ca/british-columbia/drop-bin-locations"
r1 = requests.get(url1)

soup1 = BeautifulSoup(r1.content,"lxml")
soup1.prettify();

filtered1 = soup1.find_all("tr")


'''prints out all the addresses stored
in the table on URL1'''

for sub1 in filtered1:
    inter = sub1.find_all("span")
    for sub2 in inter:
        if(len(sub2.text)>2):
            print(sub2.text)
    print("------------")