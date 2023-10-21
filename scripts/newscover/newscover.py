import json
import requests
import sys
import datetime

def fetch_latest_news(api_key,news_keywords,lookback_days):
    # Fails if news_keywords is empty
    if news_keywords == "":
        sys.error("news_keywords is empty")
        return None
    
    dates = datetime.datetime.now() - datetime.timedelta(days=lookback_days)
    # Just want the date part
    dates = str(dates).split(" ")[0]
    print(dates)
    # response = requests.get("https://newsapi.org/v2/everything?q="+news_keywords+"&from=2019-04-01&sortBy=publishedAt&apiKey="+api_key)
    # if response.status_code != 200:
    #     sys.error("Error fetching news from newsapi.org")
    #     return None
    #return response.json()

def main():
    fetch_latest_news("e7d7f14874b942fb9c02515cfe192063","bitcoin",7)
    

if __name__ == "__main__":
    main()