import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

match_id = "1"
url = "https://liiga.fi/fi/ottelut/2018-2019/runkosarja/"+match_id+"/kokoonpanot/"

page = requests.get(url).text

soup = bs(page, 'lxml')

player_dict = {}
line_1_list = list()
h_forward_list = list()
# find home team div
for home_team in soup.find_all("div", {"class": "team home"}):
    # find home team lines
    for line in home_team.find_all("div", {"class": "line"}):
        # check what line
        if home_team.find("div", {"class": "head"}).text == "1. kenttä":
            # add to that line
            line_1_list.append(home_team.find("div", {"class": "head"}).text)
            print(home_team.find("div", {"class": "head"}).text)



"""
h_fw_one_lw = soup.
h_fw_one_c =
h_fw_one_rw =
"""



home_div = soup.find("div", {"class": "team home"})
home_span = home_div.find("span", {"class": "team-name"})

away_team_div = soup.find("div", {"class": "team away"})
away_team_span = away_team_div.find("span", {"class": "team-name"})
all_divs = []
for div in soup.find_all("div"):
    all_divs.append(div.text)

# 1 forward line names dict
forw_1_dict = {}

match_dict = {"home": home_span.text, "away": away_team_span.text}
print(match_dict)