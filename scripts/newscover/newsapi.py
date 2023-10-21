import json
import requests
import sys
import datetime

def fetch_latest_news(api_key,news_keywords,lookback_days=10):
    # Fails if news_keywords is empty or there are non-alphanumeric characters
    if news_keywords == "" or news_keywords is None or not news_keywords.isalnum():
        raise ValueError("Invalid news keywords")

    if lookback_days is None:
        lookback_days = 10

    dates = datetime.datetime.now() - datetime.timedelta(days=int(lookback_days))
    # Just want the date part
    dates = str(dates).split(" ")[0]
    response = requests.get("https://newsapi.org/v2/everything?q="+news_keywords+"&from="+dates+"&sortBy=publishedAt&apiKey="+api_key)
    # Fails if response is not 200 which means the request failed
    
    # Returns a list of english articles represented as dictionaries
    return json.loads(response.text)['articles']
