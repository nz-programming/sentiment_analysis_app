## "Exciting World Cup 2022"
This application is named "Exciting World Cup 2022". 
This is the app to monitor how people feel about "FIFA World Cup 2022" using sentiment scores analyzed with Twitter.

## Demo
![Sentiment Analysis](https://user-images.githubusercontent.com/79392148/193696046-41974f30-184b-4dfb-9808-28e94f518654.gif)<br>
Youtube: https://youtu.be/nA2j7uHqDsA 

## Function
This application ...
- Describe the Twitter sentiment analysis figure in chronological order
    * retrieve tweets that contain relevant keywords of "FIFA World Cup 2022" daily by using Twitter API, and analyze Sentiment score with python
- Change the analyzed period to "Week", "Month", "Year" and show it on a chart dinamically
    * retrieve the specific data from DB responding to the request from the front end and show them on it with Javascript
- Show modal to describe the detail of each of the day
    * by clicking the item of each day on the chart, show detailed data on the day, such as "Sentiment score Top 3 Ranking"、" Number of Retweet Top 3 Ranking", "Popular Keyword", "Popular KeyPhrase"
- Add the latest data daily
    * newly analyzed data is added to DB daily and the main chart is revised every day

## How to use
- Exciting World Cup button: display the chart with all data in DB
- Week button: display the chart with data from today to 7 days ago
- Month button: display the chart with data from today to 30 days ago
- Year button: display the chart with data from today to 365 days ago

## Main Technologies
- Python 3.9.12
    * Tweepy 4.10.0, NLTK 3.7, TextBlob 0.15.3, WordCloud 1.8.2.2
    * Django 4.0, Sqlalchemy 1.4.32
- Javascript
    * Chart.js 3.9.1
- MariaDB 10.4.22
- HTML,CSS
    * Bootstrap 5.0.2

I chose these major and popular technologies used by many developers to enable me to develop this application smoothly with plenty of documents because I was not familiar with this type of development.

## Application structure
![NW_structure_diagram](https://user-images.githubusercontent.com/79392148/188246316-74ede826-b020-4a6f-8940-bbd247229ec7.png)
## Purpose of this Application
- To monitor what's going on in FIFA World Cup 2022 and find out the correlation between what happened in the event and the change of emotion of people. What's more, just I love soccer.

## Points of Development
- Making an original stopword list to increase the precision of sentiment analysis when cleaning the text content of each of the tweets
- Analyzing tweets and putting data on each day together by using JSON format before inserting data into DB to reduce data volume
- Building folder structure functionally and refactoring code without hard-coding as much as possible to maintain maintainability
## Future Update
- Deploy this app on an online server to release 
- Implement function to change analyzed period on demand
- Implement a login function to enable each of the users to change search keywords
