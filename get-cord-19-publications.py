#####################################################################
#!/usr/bin/env python3
# 

# %% required library
import pandas as pd

# %% CORD-19 Dataset
cord_19 = pd.read_csv('https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2021-07-26/metadata.csv', parse_dates=['publish_time'])

titles = cord_19[['title', 'doi', 'publish_time']]

# Drop NaN publish_time values and group by date of publication
publish_time_grouped = titles[titles['publish_time'].notnull()].groupby('publish_time').count()['title'].reset_index()

publish_time_grouped.sort_values('title', ascending=False).to_csv('data/cord_19-publications-by-date.csv', index=False)