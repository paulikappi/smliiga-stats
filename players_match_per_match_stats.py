import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# scraping all player data
season = "2018-2019"
url = "https://liiga.fi/fi/pelaajat/"+season+"/"

# generate html
page = requests.get(url).text
data = pd.read_html(page, decimal=',')
soup = BeautifulSoup(page, "lxml")

# find all links by url, add link texts to list
player_name_list = list()
for player_link_spam in soup.find_all('a', href=re.compile('^/fi/pelaajat/')):
    player_name_list.append(player_link_spam.text)

# Drop first "Pelaajat" string from name list
if player_name_list[0] == "Pelaajat":
    player_name_list = player_name_list[1:]

# find player ids by css, filter digits and make a list
player_id_spam = str(soup.select("a[href*=pelaaja]"))
digits = re.compile(r"\d+")
player_id_list = list(digits.findall(player_id_spam))

# generate dictionary from two lists for fun
player_tuple = zip(player_name_list, player_id_list)
player_dictionary = {}

for key, value in player_tuple:
    if key in player_dictionary:
        pass
    else:
        player_dictionary[key] = value

# scrape all other data from table




# create pandas dataframe and add data as columns
zip_list = list(zip(player_name_list, player_id_list))
df = pd.DataFrame(zip_list, columns=["name", "id"])
df.to_csv("player_database"+season+".csv")
