#this file contains all the functions concerned with scraping
#html table sites
#google map sites
#get data
#misc scraper

import requests
import json
from bs4 import BeautifulSoup
from bin import Bin


#Salvation Army Thrift Store
url1 = "https://www.thriftstore.ca/british-columbia/drop-bin-locations"
r1 = requests.get(url1)

soup1 = BeautifulSoup(r1.content,"lxml")
soup1.prettify();

filtered1 = soup1.find_all("tr")


'''prints out all the addresses stored
in the table on URL1'''

list = []

for td in filtered1:
	inter = td.find_all("span")
	count = 0
	addBin = Bin("", "", "", "", "", "", "")
	while (count <= 3):
		value = inter[count].text
		if(count == 0):
			addBin.name = value
		elif (count == 1):
			addBin.company = value
		elif (count == 2):
			addBin.address = value
		else:
			addBin.city = value
		count += 1
	list.append(addBin)

for item in list:
	print(item)