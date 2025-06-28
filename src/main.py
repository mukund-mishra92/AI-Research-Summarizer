from fetch.arxiv_fetcher import fetch_arxiv_articles
from summarize.summarizer import summarize_text
from storage.database import init_db, save_article
from notify.email_notifier import notify_user

def main():
    init_db()

    print("🔍 Fetching articles from arXiv...")
    articles = fetch_arxiv_articles()

    print(f"✍️ Summarizing and saving {len(articles)} articles...")
    for art in articles:
        art["summary"] = summarize_text(art["summary"])
        save_article(art)

    # ⬇️ Send daily digest email
    notify_user()

if __name__ == "__main__":
    main()
