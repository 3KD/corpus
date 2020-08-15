#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Index_of_branches_of_science'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

ls = []

group = soup.find_all(class_='mw-redirect', )

#print(group)

"""def reverse(string):
	string = string[::-1]
	list.append(string)"""

for i in group:
	print(i)
	
#print(group)	

#print(group.find(title))

#print(soup.prettify)

#print(soup.find_all("li", text="ology"))
