## Overview
This application is named "Exciting World Cup 2022". 
This is the app to monitor how people feel to "FIFA World Cup 2022" using sentiment score analyzed with Tweitter.

## Demo

## Functioin
This application ...
- Describe twitter sentiment analysis figure in chronological order
    retrieve tweets which contain relevant keyword of "FIFA World Cup 2022" daily by using Twitter API, and analyze Sentiment score with python
- Change the analyzed period to "Week", "Month", "Year" and show it on a chart dinamically 
    retrive the specific data from DB responding to the request from front end and show them on front end with Javascript
- Show modal to describe the detail of each of the days
    by clicking the item of the each day on chart, show detail data on the day, such as "Sentiment score Top 3 Raning"、"Number of Retweet Top 3 Raning", "Popular Keyword", "Popular KeyPhrase"
- Add the latest data on a daily basis
    new analyzed data is add to DB daily and main chart is revised every day

## Main Technologies
- Python 3.9.12 
    Tweepy 4.10.0, NLTK 3.7, TextBlob 0.15.3, WordCloud 1.8.2.2
    Django 4.0, sqlalchemy 1.4.32
- Javascript
    Chart.js 3.9.1
- MariaDB 10.4.22
- HTML,CSS
    Bootstrap 5.0.2


