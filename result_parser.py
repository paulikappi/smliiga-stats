import requests
import pandas as pd
import numpy as np
enc = "utf-8"

url = "https://liiga.fi/fi/ottelut/2018-2019/runkosarja/"

page = requests.get(url).text

data = pd.read_html(page, encoding=enc)
data[0].to_csv('webfile.csv', encoding=enc)

df = pd.read_csv("webfile.csv", encoding=enc)

# clean data, name columns
df.drop(["Unnamed: 0","Aika", "Linkit"], axis=1, inplace=True)
df.columns = ['match_id', 'date', 'teams', 'result', 'overtime', 'audience']
# df.drop(["match"], axis=1, inplace=True)

# split team columns
df['home'], df['away'] = df['teams'].str.split(' ', 1).str
df.drop(["teams"], axis=1, inplace=True)

# split goal columns
df['h_goal'], df['a_goal'] = df['result'].str.split(' ', 1).str
df.drop(["result"], axis=1, inplace=True)

# clean goal data
df["a_goal"] = df["a_goal"].map(lambda x: str(x)[-1:])
df["away"] = df["away"].map(lambda x: str(x)[4:])

# fill empty dates
df['date'] = df['date'].fillna(method='ffill')


df.to_csv("file.csv", encoding=enc)
