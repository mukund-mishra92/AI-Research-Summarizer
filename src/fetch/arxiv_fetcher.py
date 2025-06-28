import requests
import feedparser
from utils.config import ARXIV_CATEGORIES

def fetch_arxiv_articles():
    all_articles = []
    base_url = "http://export.arxiv.org/api/query?search_query=cat:{}&start=0&max_results=5"

    for cat in ARXIV_CATEGORIES:
        url = base_url.format(cat)
        feed = feedparser.parse(requests.get(url).text)

        for entry in feed.entries:
            article = {
                "id": entry.id.split("/")[-1],
                "title": entry.title,
                "summary": entry.summary,
                "published": entry.published,
                "source": "arxiv"
            }
            all_articles.append(article)

    return all_articles
