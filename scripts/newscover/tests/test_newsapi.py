import unittest
import datetime
from scripts.newscover.newsapi import fetch_latest_news

class Test(unittest.TestCase):
    def news_keyword_Is_None(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = ""
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)

    def news_keyword(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "jesus"
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)
        
class TestLookBack(unittest.TestCase):
    def lookback_with_days(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "tesla"
        lookback_days = 5
        oldest_allowed_date = datetime.datetime.now() - datetime.timedelta(days=int(lookback_days))
        news = fetch_latest_news(api_key, news_keywords, lookback_days)
        for article in news:
            article_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertGreaterEqual(article_date, oldest_allowed_date)


    def lookback_without_days(self):
        api_key="e7d7f14874b942fb9c02515cfe192063"
        news_keywords= "tesla"
        oldest_allowed_date = datetime.datetime.now() - datetime.timedelta(days=int(lookback_days))
        news = fetch_latest_news(api_key, news_keywords, lookback_days)
        for article in news:
            article_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertGreaterEqual(article_date, oldest_allowed_date)


class TestNonAlpha(unittest.TestCase):        
    def news_keyword_one_nonAlpha(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "tesla@123"
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)

    def news_keyword_all_nonAlpha(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "@@@"
        self.assertFail()
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)


