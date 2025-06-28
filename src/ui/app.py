import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from storage.database import get_recent_articles
from notify.email_notifier import send_email_summary

st.set_page_config(page_title="🧠 AI Daily Research Digest", layout="wide")
st.title("📰 Daily AI News Summary")

# Fetch recent articles from DB
articles = get_recent_articles(limit=10)

if not articles:
    st.warning("No articles found. Please run the fetch script first.")
else:
    selected_articles = []
    for art in articles:
        with st.expander(f"📘 {art['title']} ({art['source']})"):
            st.write(f"🕒 Date: {art['published']}")
            st.write(f"📝 Summary:\n{art['summary']}")
            if st.checkbox(f"✉️ Send this to customers", key=art["id"]):
                selected_articles.append(art)

    # Email block
    st.markdown("---")
    st.subheader("📧 Email Summary")
    email = st.text_input("Customer Email Address")
    if st.button("🚀 Send Email Summary"):
        if email and selected_articles:
            body = "\n\n".join([f"{a['title']}:\n{a['summary']}" for a in selected_articles])
            send_email_summary(email, "Your Daily AI Research Summary", body)
            st.success("✅ Email sent successfully!")
        else:
            st.error("Please select articles and enter an email address.")
