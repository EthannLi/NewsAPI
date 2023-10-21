import unittest
import datetime
from newscover.newsapi import fetch_latest_news

class test_Keyword(unittest.TestCase):
    def test_news_keyword_Is_Empty(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = ""
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)

    def test_news_keyword_is_None(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = None
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key,news_keywords)
        
class test_LookBack(unittest.TestCase):
    def test_lookback_with_days(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "tesla"
        lookback_days = 5
        oldest_allowed_date = datetime.datetime.now() - datetime.timedelta(days=int(lookback_days))
        news = fetch_latest_news(api_key, news_keywords, lookback_days)
        for article in news:
            article_date = datetime.datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertGreaterEqual(article_date, oldest_allowed_date)

    def test_lookback_without_days(self):
        api_key="e7d7f14874b942fb9c02515cfe192063"
        news_keywords= "tesla"
        oldest_allowed_date = datetime.datetime.now() - datetime.timedelta(10)
        news = fetch_latest_news(api_key, news_keywords)
        for article in news:
            article_date = datetime.datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertGreaterEqual(article_date, oldest_allowed_date)

class test_NonAlpha(unittest.TestCase):        
    def test_news_keyword_one_nonAlpha(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "tesla@123"
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)

    def test_news_keyword_all_nonAlpha(self):
        api_key = "e7d7f14874b942fb9c02515cfe192063"
        news_keywords = "@@@"
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key, news_keywords)

if __name__ == "__main__":
    unittest.main()