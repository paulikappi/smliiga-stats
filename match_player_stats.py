from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import re

url = "https://liiga.fi/fi/ottelut/2018-2019/runkosarja/1/tilastot/"
page = requests.get(url).text
data = pd.read_html(page)
soup = bs(page, "lxml")


home_team = soup.find("div", {"class": "team home"}).text
away_team = soup.find("div", {"class": "team away"}).text
player_stats = list()
td_list = list()


home_player_table = soup.find("table", {"class": "player-stats"})
player_rows = home_player_table.find_all("tr")
for tr in player_rows:
    td = tr.find_all("td")
    row = [tr.text for tr in td]
    player_stats.append(row)
df = pd.DataFrame(player_stats,
                  columns=[
                    "name",
                    "number",
                    "place",
                    "goals",
                    "pass",
                    "points",
                    "penalties",
                    "plus",
                    "minus",
                    "plus_minus",
                    "power_play_goals",
                    "shorthanded_goals",
                    "victory_goals",
                    "shots",
                    "shot_percent",
                    "face-offs",
                    "face-off_percent",
                    "play_time"
                  ])

df.to_csv('match_player_stats.csv')
