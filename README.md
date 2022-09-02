## Overview
This application is named "Exciting World Cup 2022". 
This is the app to monitor how people feel to "FIFA World Cup 2022" using sentiment score analyzed with Tweitter.

## Demo

## Functioin
This application ...
- Describe twitter sentiment analysis figure in chronological order<br>
    retrieve tweets which contain relevant keyword of "FIFA World Cup 2022" daily by using Twitter API, and analyze Sentiment score with python
- Change the analyzed period to "Week", "Month", "Year" and show it on a chart dinamically<br>
    retrive the specific data from DB responding to the request from front end and show them on front end with Javascript
- Show modal to describe the detail of each of the days<br>
    by clicking the item of the each day on chart, show detail data on the day, such as "Sentiment score Top 3 Raning"、"Number of Retweet Top 3 Raning", "Popular Keyword", "Popular KeyPhrase"
- Add the latest data on a daily basis<br>
    new analyzed data is add to DB daily and main chart is revised every day

## How to use
- Exciting World Cup button: desplay the chart with all data in DB
- Week button: desplay the chart with data over from today to 7 days ago
- Month button: desplay the chart with data over from today to 30 days ago
- Year button: desplay the chart with data over from today to 365 days ago

## Main Technologies
- Python 3.9.12<br>
    Tweepy 4.10.0, NLTK 3.7, TextBlob 0.15.3, WordCloud 1.8.2.2
    Django 4.0, sqlalchemy 1.4.32
- Javascript<br>
    Chart.js 3.9.1
- MariaDB 10.4.22
- HTML,CSS<br>
    Bootstrap 5.0.2

I chose these major and popular technologies by many developers to enable me to develop this application smoothly with plenty of documents because I'm not familiar with this type of development.

## Application structure

## Purpose of this Application
- To monitor what's going on in FIFA World Cup 2022 and find out corralation between what happen in the event and change of emotion of people. What's more, just I love succor.

## Points of Development
- Making original stopword list to increase the precision of sentiment analysis when cleaning text content each op the tweet
- Analyzing tweets and put data on each day together by using JSON format before inserting data into DB to reduce data volume
- Building folda structure functionally and refactor code without hard coding as much as possible to maintain maintainability
## Future Update
- Deploy this app on an online server to release 
- Impliment function to change analyzed period on demand
- Impliment login function to enable each of the user to change search keywords
