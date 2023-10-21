import unittest
import datetime
from scripts.newscover.newsapi import fetch_latest_news

class TestNewsAPI(unittest.TestCase):
    def news_keyword_Is_None():
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = ""
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)

    def lookback_days(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "tesla"
        lookback_days = 5
        oldest_allowed_date = datetime.datetime.now() - datetime.timedelta(days=lookback_days)
        news = fetch_latest_news(api_key, news_keywords, lookback_days)
        for article in news:
            article_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertGreaterEqual(article_date, oldest_allowed_date)
        
    def news_keyword_nonAlpha():
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "tesla@123"
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)