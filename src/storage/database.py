import sqlite3
from utils.config import DB_PATH

import sqlite3
from .schema import DB_PATH

# def get_recent_articles(limit=10):
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     cursor = conn.cursor()

#     cursor.execute("SELECT title, summary, published, source FROM articles ORDER BY published DESC LIMIT ?", (limit,))
#     rows = cursor.fetchall()
#     conn.close()
#     return [dict(row) for row in rows]

def get_recent_articles(limit=10):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles ORDER BY published DESC LIMIT ?", (limit,))
    articles = cursor.fetchall()
    conn.close()
    return [dict(row) for row in articles]


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id TEXT PRIMARY KEY,
            title TEXT,
            summary TEXT,
            published TEXT,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_article(article):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO articles (id, title, summary, published, source)
        VALUES (?, ?, ?, ?, ?)
    """, (article["id"], article["title"], article["summary"], article["published"], article["source"]))
    conn.commit()
    conn.close()

# def get_recent_articles(limit=10):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("""SELECT * FROM articles ORDER BY published DESC LIMIT ?""", (limit,))
#     articles = c.fetchall()
#     conn.close()
#     return articles
