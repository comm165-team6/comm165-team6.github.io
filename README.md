# <b>Analyzing Criminal Activity during COVID-19</b>
#### Papa Asibuo, Kyra Hollenbach, Natalie Morgan, and Jenna Simon

### <b>Purpose</b>

### <b>Data Source</b>

We used two main data sources for analyzing criminal activity during the pandemic. Our data on specific records of criminal activity came from Open Data DC. Datasets on crime incidents by year are available at the following links:

[2017](https://opendata.dc.gov/datasets/crime-incidents-in-2017/data?geometry=-77.369%2C38.806%2C-76.660%2C38.993)
[2018](https://opendata.dc.gov/datasets/crime-incidents-in-2018/data?geometry=-77.369%2C38.806%2C-76.660%2C38.993)
[2019](https://opendata.dc.gov/datasets/crime-incidents-in-2019/data?geometry=-77.358%2C38.806%2C-76.671%2C38.993&orderBy=REPORT_DAT)
[2020](https://opendata.dc.gov/datasets/crime-incidents-in-2020/data?geometry=-77.358%2C38.806%2C-76.671%2C38.993&orderBy=REPORT_DAT)
[2021](https://opendata.dc.gov/datasets/crime-incidents-in-2021/data?geometry=-77.358%2C38.806%2C-76.671%2C38.993&orderBy=REPORT_DAT)

Our second source came from scraping Twitter data. In addition to actual records of criminal activity, we were interested in seeing how frequently people were discussing crime on public platforms. To do this, we collected a count of how many tweets in the months of January, February, and March contained keywords relating to crime, for each year from 2012 through 2021. These keywords included "crime", "robbery", "theft", "arson", "assault", and "arrest." As an example of the script we used to collect this data, the following code would receive all tweets in the DC area that contained the word "arrest," from January through March 2021:

```
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import tweepy

# Creating list to append tweet data
tweets_list = []

# Using TwitterSearchScraper to scrape records
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('arrest near:"Washington, D.C." since:2021-01-01 until:2021-04-01').get_items()):
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
tweets_df = pd.DataFrame(tweets_list, columns = ['Datetime', 'Tweet_id', 'Text', 'Username'])

print(tweets_df)
```

### <b>Crime Rate Findings: Overall Activity Decreases</b>

### <b>Twitter Activity: Crime Discussion Increases</b>

### <b>Discussion and Conclusion</b>
