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
To get an overall understanding of how crime has changed over the course of the pandemic, we created visualizations using crime data from past years in the “pre-pandemic” era (2017,2018, 2019) and compared to it pandemic era, 2020. 
<div class='tableauPlaceholder' id='viz1620137317783' style='position: relative'><noscript><a href='#'><img alt='How Crime Counts Have Changed in Washington D.C. Between 2017-2020 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cr&#47;CrimeCountChange&#47;CrimeCountChange&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CrimeCountChange&#47;CrimeCountChange' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cr&#47;CrimeCountChange&#47;CrimeCountChange&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1620137317783'); var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px'; var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>

After analyzing these different visualizations, it is clear that there is an overall decrease in crimes comparing pre-pandemic data to pandemic data. In 2018, there were 33,035 crimes committed in Washington D.C., 33,755 in 2018, 33,895 in 2019, and 27,871 in 2020. 2020 is the first year to drop below 33,000 in the years we are analyzing, and compared to the average number of crimes between 2017-2019, there was a 20.417% decrease in crime in 2020. Although there is a decrease in overall crime, there was a specific significant increase in motor vehicle theft in 2020 compared to 2017, 2018, 2019. In fact, compared to pre-pandemic averages, there was a 34% increase in 2020. 

For some types of crime, there were no significant increases or decreases. For example, arson, assault with a dangerous weapon, burglary and homicide stayed at similar levels to years previous. Theft, sex abuse and robbery had significant decreases to years prior.


### <b>Crime Map According to Category in DC</b>

These maps show the different types of crimes and where they were committed within Washington DC. This visualization is divided into 4 maps: one for each year from 2017 to 2021(May). 


<div class='tableauPlaceholder' id='viz1619994780963' style='position: relative'><noscript><a href='#'><img alt='Crime in Washington DC over the years ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cr&#47;CrimeinWashingtonDC2017-2021&#47;CrimeinWashingtonDCovertheyears&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CrimeinWashingtonDC2017-2021&#47;CrimeinWashingtonDCovertheyears' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cr&#47;CrimeinWashingtonDC2017-2021&#47;CrimeinWashingtonDCovertheyears&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1619994780963'); var vizElement = divElement.getElementsByTagName('object')[0]; vizElement.style.width='1016px';vizElement.style.height='991px'; var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>

This visualization revealed the areas of DC that are highly prone to crime; the maps all followed the general trend of the same areas almost constantly covered in crime. Over the years, auto theft became increasingly prevalent in ward 2 (the northern parts of DC), while assault with a dangerous weapon had a constant dominance in all other wards in DC. It was noteworthy that most of the same types of crimes occured in the same places every year.

The data for this map was last updated on May 2nd 2021.


### <b>Crime by Time, Location, and Ward in 2021</b>
The following is a visualization showing crime by type and time by ward in Washington, DC. The neighborhoods within each ward are as follows:

<b>Ward 1:</b> Adams Morgan, Columbia Heights, Kalorama Triangle, LeDroit Park, Mount Pleasant, Park View, Pleasant Plains, Shaw, U Street NW corridor

<b>Ward 2:</b> Burleith, Chinatown, Downtown, Dupont Circle, Foggy Bottom, Georgetown, Logan Circle, National Mall, Penn Quarter, Shaw, Kalorama, U Street NW corridor, West End

<b>Ward 3:</b> American University Park, Cathedral Heights, Chevy Chase, Cleveland Park, Forest Hills, Foxhall Crescent, Foxhall Village, Friendship Heights, Glover Park, Kent, Massachusetts Avenue Heights, McLean Gardens, North Cleveland Park, Observatory Circle, Palisades, Spring Valley, Tenleytown, Wakefield, Wesley Heights, Woodley Park

<b>Ward 4:</b> Barnaby Woods, Brightwood, Brightwood Park, Chevy Chase, Colonial Village, Crestwood, Fort Totten, Hawthorne, Lamond-Riggs, Manor Park, Petworth, Queens Chapel, Shepherd Park, 16th Street Heights, Takoma

<b>Ward 5:</b> Arboretum, Bloomingdale, Brentwood, Brookland, Carver-Langston, Eckington, Edgewood, Fort Lincoln, Fort Totten, Gateway, Ivy City, Langdon, Michigan Park, North Michigan Park, Pleasant Hill, Queens Chapel, Stronghold, Trinidad, Truxton Circle, Woodridge

<b>Ward 6:</b> Barney Circle, Capitol Hill, Capitol Riverfront, Hill East, H Street NE corridor, Kingman Park, L’Enfant Plaza, Mount Vernon Triangle, Navy Yard, Near Northeast, NoMa, Shaw, Southwest Waterfront

<b>Ward 7:</b> Benning Heights, Benning Ridge, Benning, Burrville, Capitol View, Civic Betterment, Deanwood, Dupont Park, Eastland Gardens, Fairfax Village, Fairlawn, Fort Davis Park, Good Hope, Greenway, Hillcrest, Kenilworth, Kingman Park, Lincoln Heights, Marshall Heights, Mayfair, Naylor Gardens, Northeast Boundary, Penn Branch, Randle Highlands, River Terrace, Skyland, Twining

<b>Ward 8:</b> Anacostia, Barry Farm, Bellevue, Buena Vista, Congress Heights, Douglass, Fairlawn, Garfield Heights, Joint Base Anacostia-Bolling, Shipley Terrace, Skyland, Washington Highlands, Woodland

<div class='tableauPlaceholder' id='viz1620145370270' style='position: relative'><noscript><a href='#'><img alt='2021 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DC&#47;DCCrime2021&#47;2021Story&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DCCrime2021&#47;2021Story' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DC&#47;DCCrime2021&#47;2021Story&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1620145370270'); var vizElement = divElement.getElementsByTagName('object')[0]; vizElement.style.width='1016px';vizElement.style.height='991px'; var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>

### <b>Twitter Activity: Crime Discussion Increases</b>

As explained in the "Data Source" section, we used the snscrape Python library to get the count of tweets that contained certain keywords in the D.C. area, from January through March over the past 10 years. The chart below displays the frequencies of these keywords, grouped by year.

<iframe width="990" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSyletTaL0iV8-2wBCnyWCRGsxeugc9QTDFRjrPpf-iKwYh4zcXPcU7hmeoxnUoZLd3H5qEmLiV3Wnh/pubchart?oid=1939436595&amp;format=interactive"></iframe>


The chart shows a gradual increase in crime-related discussion on Twitter over the past three years, specifically in 2020 and 2021. The crime discussion on Twitter in 2020 was the highest it had been since 2012. 

### <b>Discussion and Conclusion</b>

We were initially surprised by the conflict between the recorded criminal activity data, and the Twitter data. While crime levels have been lower during the pandemic, discussion of crime on public platforms such as Twitter has increased. We believe this could be indicitive of general feelings of fear and uncertainty that have accompanied the pandemic. As anxiety around and discussion of crime increases along with the pandemic anxiety, we are more likely to see bursts of violent rehtoric and activity. In the interest of public safety, it is important to be cognizant of how times of uncertainty can influence public behavior.
