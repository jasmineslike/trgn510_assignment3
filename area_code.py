#!/usr/bin/python

import re

def area_code():
	file = open("phoneNumbers.txt", "r")
	for phone in file:
		match = re.search(r'(\d{3})', phone)
		
		if match:
			print(match.group())
		else:
			print("No match!!")

	file.close()

area_code()
  		
