import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request
import csv

enc = "utf-8"

url = "http://www.oddsportal.com/hockey/finland/liiga/"
web = urllib.request.urlopen(url)

soup = BeautifulSoup(web, 'lxml')

file = 'odds_portal.csv'


page = requests.get(url).content

table = soup.find_all("table", {"id": "tournamentTable"})


tr_list = soup.find_all("tr", {"class": "odd"})
td_list = soup.find_all("td", {"class": "odd-nowrp"})
print(tr_list)
