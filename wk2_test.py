import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_by_traffic-related_death_rate"

# 1. Getting HTML w/a browser-like User-Agent bc otherwise it's forbidden 🙄 
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0 Safari/537.36"
    )
}
resp = requests.get(url, headers=headers)
resp.raise_for_status()   # will raise if still 403/404/etc...

# 2. Using read_html on the HTML string
tables = pd.read_html(resp.text)
df = tables[0]   # main table

print(df.head())


round(asia_2019_avg)
