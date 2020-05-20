import pandas as pd
import requests
from bs4 import BeautifulSoup

season = "2018-2019"
match_id = "421"
url = "https://liiga.fi/fi/ottelut/"+season+"/runkosarja/"+match_id+"/seuranta/"

page = requests.get(url).content
data = pd.read_html(page, decimal=',')
data[0].to_csv("match_details_" + season + "_" + match_id + ".csv", sep=",", decimal=".")

soup = BeautifulSoup(page, "lxml")
print(soup)