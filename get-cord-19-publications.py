#####################################################################
#!/usr/bin/env python3
# 

# %% required library
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# CORD-19 Historical Releases
url = 'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html'

r = requests.get(url)
soup = BeautifulSoup(r.text)
latest_date = soup.td.get_text()

# create date column
date = str(datetime.date.today())

# %% Load dataframe of metadata from CORD-19 Dataset
cord_19 = pd.read_csv('https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/' + latest_date + '/metadata.csv', parse_dates=['publish_time'])
titles = cord_19[['title', 'doi', 'publish_time']]

# Drop NaN publish_time values and group by date of publication
publish_time_grouped = titles[titles['publish_time'].notnull()].groupby('publish_time').count()['title'].reset_index()

publish_time_grouped.sort_values('title', ascending=False).to_csv('data/cord_19-publications-by-date.csv', index=False)
