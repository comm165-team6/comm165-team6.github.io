# <b>Analyzing Criminal Activity during COVID-19</b>
#### Papa Asibuo, Kyra Hollenbach, Natalie Morgan, and Jenna Simon

### <b>Purpose</b>

In this project, we analyze how different aspects of crime have changed in Washington D.C. over the course of the COVID-19 pandemic. We chose Washington D.C. because it is one the the most diverse metro areas in the United States. Additionally, we were curious if the sudden spike in violent activity seen in D.C. on January 6th was preceded by any noticeable increases in crime in the area. We wanted to focus on a city because larger populations would probably allow us to have a more specific and accurate scope of data. Specifically, we will be analyzing the changes in overall crime rates and how different types of crime rates have fluctuated since the pandemic.

Crime is a huge aspect and consideration of the public in regard to relevant human safety, and understanding the fluctuations in crime trends and rates may help people have a prepared response. It is also interesting to see if there’s any underlying reasons for spikes or decreases in crimes because of the pandemic. We are predicting/expecting certain crime rates of specific types of crimes to be at a fluctuation compared to years without the COVID-19 pandemic.

### <b>Data Source</b>

We used two main data sources for analyzing criminal activity during the pandemic. Our data on specific records of criminal activity came from Open Data DC. Datasets on crime incidents by year are available at the following links:

* [2017](https://opendata.dc.gov/datasets/crime-incidents-in-2017/data?geometry=-77.369%2C38.806%2C-76.660%2C38.993)
* [2018](https://opendata.dc.gov/datasets/crime-incidents-in-2018/data?geometry=-77.369%2C38.806%2C-76.660%2C38.993)
* [2019](https://opendata.dc.gov/datasets/crime-incidents-in-2019/data?geometry=-77.358%2C38.806%2C-76.671%2C38.993&orderBy=REPORT_DAT)
* [2020](https://opendata.dc.gov/datasets/crime-incidents-in-2020/data?geometry=-77.358%2C38.806%2C-76.671%2C38.993&orderBy=REPORT_DAT)
* [2021](https://opendata.dc.gov/datasets/crime-incidents-in-2021/data?geometry=-77.358%2C38.806%2C-76.671%2C38.993&orderBy=REPORT_DAT)

Our second source came from scraping Twitter data using the snscrape Python library. In addition to actual records of criminal activity, we were interested in seeing how frequently people were discussing crime on public platforms. To do this, we collected a count of how many tweets in the months of January, February, and March contained keywords relating to crime, for each year from 2012 through 2021. These keywords included "crime", "robbery", "theft", "arson", "assault", and "arrest." As an example of the script we used to collect this data, the following code would receive all tweets in the DC area that contained the word "arrest," from January through March 2021:

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

As explained in the "Data Source" section, we used the snscrape Python library to get the count of tweets that contained certain keywords in the D.C. area, from January through March over the past 10 years. The chart below displays the frequencies of these keywords, grouped by year.

<iframe width="990" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSyletTaL0iV8-2wBCnyWCRGsxeugc9QTDFRjrPpf-iKwYh4zcXPcU7hmeoxnUoZLd3H5qEmLiV3Wnh/pubchart?oid=1939436595&amp;format=interactive"></iframe>


The chart shows a gradual increase in crime-related discussion on Twitter over the past three years, specifically in 2020 and 2021. The crime discussion on Twitter in 2020 was the highest it had been since 2012. 

### <b>Discussion and Conclusion</b>
