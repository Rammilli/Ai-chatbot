import pytest
from src.pipeline.collector import collect_news

def test_collect_news_returns_list():
    """
    Ensure the RSS data collector correctly formats its output 
    as a list of dictionaries.
    """
    articles = collect_news()
    assert isinstance(articles, list)
