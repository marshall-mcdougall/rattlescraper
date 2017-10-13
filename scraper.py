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
	addBin = Bin("", "", "", "", "", "")
	while (count <= 3):
		value = inter[count].text.strip()
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

#Inclusion BC & CPABC Clothing
url2 = "http://www.google.com/maps/d/kml?mid=1kqVfqYiPtnqrO8L5zC_yVkAiwB0&forcekml=1"
url3 = "https://www.google.com/maps/d/kml?mid=1ekVOoKgoAW2vIjiDh3DmP4OU04g&forcekml=1"
r2 = requests.get(url2)
r3 = requests.get(url3)

soup2 = BeautifulSoup(r2.content,"lxml")
soup3 = BeautifulSoup(r3.content,"lxml")

filtered2 = soup2.find_all("placemark")
filtered3 = soup3.find_all("placemark")

for item in filtered2:
	addBin = Bin("", "", "", "", "", "")
	addBin.address = item.find_all("name")[0].text.strip()
	addBin.coordinate = item.find_all("coordinates")[0].text.strip()
	list.append(addBin)

for item in filtered2:
	addBin = Bin("", "", "", "", "", "")
	addBin.address = item.find_all("name")[0].text.strip()
	addBin.setCoordinate = item.find_all("coordinates")[0].text.strip()
	list.append(addBin)

for item in list:
	print("-----------------------")
	print(item)
	print("-----------------------")
