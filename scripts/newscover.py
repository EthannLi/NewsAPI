import json
import requests

def fetch_latest_news(api_key,news_keywords,lookback_days=10):
    response = requests.get("https://newsapi.org/v2/everything?q="+news_keywords+"&from=2021-05-01&sortBy=publishedAt&apiKey="+api_key)
    return response.json()



