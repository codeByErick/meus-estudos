# A tool that verify if a directory exists in a website

import sys
import requests

try:
	list = sys.argv[2]
	site = sys.argv[1]
except:
	list = open("wordlists/Directories_Common.txt")
	site = str(input("url: "))

if "http" not in site:
	site = "http://" + site

for diretorio in list.readlines():
	arq = diretorio.replace("\n", "")
	url = site + "/" + arq
	r = requests.get(url)
	code = r.status_code
	
	if code != 404:
		print(url, "---->", "CODE:", code)
