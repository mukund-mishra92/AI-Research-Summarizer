import os

TOPICS = ["AI", "machine learning", "computer vision", "deep learning"]
ARXIV_CATEGORIES = ["cs.AI", "cs.CV", "cs.LG"]
NOTIFY_EMAIL = os.getenv("NOTIFY_EMAIL", "you@example.com")
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "articles.db")
