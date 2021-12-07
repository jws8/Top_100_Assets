#Top 100 Assets by Market Cap Web Scraper
#Date: 12/7/2021
#Author: Joshua W Smith (https://github.com/jws8)

import requests
from bs4 import BeautifulSoup as BS

url = "https://companiesmarketcap.com/assets-by-market-cap/"
data = requests.get(url).text
doc = BS(data, "html.parser")
#tbody = doc.tbody
#trs = tbody.contents
price_dict = {}
price_list = []

#with open("marketcap.txt", "w") as f:
    #f.write(trs[0].next_sibling.prettify())
#for tr in trs[1:15]: 
    #for td in tr:
        #print(type(td))
prices = doc.find_all("td", attrs={"class":"td-right"})
names = doc.find_all("div", attrs={"class": "company-name"})

count = 0
for i in range(1,len(prices)):
    if count > 1: 
        i+=1
        count = 0
    else:
        price_list.append(prices[i].string)
        count+=1
j = 1
for i in range(len(names)):
    #print(str(i+1) + ". " + str(names[i].string))
    price_dict[names[i].string] = ("#" + str(i+1) + ") " + str(price_list[j-1].string) + ": " + str(price_list[j].string))
    j+=2
print("Top 100 Assets by Market Cap: " + "\n" + str(price_dict))






    

