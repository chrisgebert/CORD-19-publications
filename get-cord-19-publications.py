########################################################################
#!/usr/bin/env python3
######################################################################## 

# %% required libraries
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

# Get date of latest release from CORD-19 Historical Releases
url = 'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html'
r = requests.get(url)
soup = BeautifulSoup(r.text)
latest_date = soup.td.get_text()

# Get date and create column titles
date = str(datetime.date.today() - datetime.timedelta(days = 1))
describe = ['Date', 'Article Count', 'Mean Author Count', 'Std Author Count', 'Min Author Count', \
'25% Percentile', '50% Percentile', '75% Percentile', 'Max Author Count']

# Check if latest dataset date is not in historical data file
historical_data = pd.read_csv('data/CORD-19-historical-releases.csv', dtypes={'Article Count': 'int64', \
'Min Author Count': 'int64', '25% Percentile': 'int64', '50% Percentile': 'int64', '75% Percentile': 'int64', \
'Max Author Count': 'int64'})

if latest_date != historical_data.loc[0]['Date']:
  # Load dataframe of metadata from CORD-19 Dataset and process author data
  cord_19 = pd.read_csv('https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/' + latest_date + \
  '/metadata.csv', parse_dates=['publish_time'])
  cord_19['author_list'] = cord_19['authors'].astype(str).apply(lambda x: x.split(';'))
  cord_19['author_count'] = cord_19['author_list'].str.len()
  row = cord_19['author_count'].describe().tolist()
  row.insert(0, latest_date)
  latest_data = dict(zip(describe, row))
  
  # Append latest data and write file to repo
  historical_data = historical_data.append(latest_data, ignore_index=True).sort_values('Date', ascending=False)
  historical_data.to_csv('data/CORD-19-historical-releases.csv', index=False)