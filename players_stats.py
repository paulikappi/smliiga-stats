import pandas as pd
import requests

season = "2018-2019"
url = "https://liiga.fi/fi/tilastot/"+season+"/runkosarja/pelaajat/"
page = requests.get(url).content
data = pd.read_html(page, decimal=',')
data[0].to_csv('player_stats_'+season+'.csv', sep=',', decimal='.')

pro_url = "https://liiga.fi/fi/tilastot/"+season+"/runkosarja/pelaajat/" \
          "?team=&position=all&home_away=&player_stats=enhanced&sort=P#stats-wrapper"

pro_page = requests.get(pro_url).content
pro_data = pd.read_html(pro_page, decimal=',')
pro_data[0].to_csv('player_stats_pro_'+season+'.csv', sep=',', decimal='.')
