import streamlit as st
from storage.database import get_recent_articles
from notify.email_notifier import send_email_summary
from agent.rag_chain import build_qa_agent

# --- UI Configuration ---
st.set_page_config(page_title="🧠 AI Research Summarizer", layout="wide")
st.title("🧠 Balmukund's Research Assistant Dashboard")

# --- Sidebar Settings ---
st.sidebar.header("⚙️ Settings")
summary_limit = st.sidebar.selectbox("Number of articles to display", [5, 10, 20, 50], index=1)
digest_type = st.sidebar.radio("Digest Type", ["Daily", "Weekly"])
st.sidebar.markdown("---")
custom_email = st.sidebar.text_input("Customer Email")
send_email_btn = st.sidebar.button("📧 Send Summary to Customer")

# --- Article Display ---
st.subheader(f"📘 {digest_type} Digest – Latest {summary_limit} Articles")
articles = get_recent_articles(limit=summary_limit)

if not articles:
    st.warning("No articles available. Please run the fetcher script first.")
else:
    for art in articles:
        with st.expander(f"{art['title']} ({art['published']})"):
            st.write(f"📝 **Summary**:\n\n{art['summary']}")
            st.caption(f"🗞 Source: {art['source']}")

    # Email sending
    if send_email_btn and custom_email:
        body = "\n\n".join([f"{a['title']}\n{a['summary']}" for a in articles])
        send_email_summary(
            to_email=custom_email,
            subject=f"{digest_type} AI Research Digest",
            body=body
        )
        st.success(f"📨 Summary sent to {custom_email}")

# --- RAG Q&A Section ---
st.markdown("---")
st.subheader("💬 Ask a Question about Recent Research (RAG)")
user_query = st.text_input("Type your question here (e.g., What's new in LLMs?)")

if user_query:
    with st.spinner("Thinking..."):
        qa_agent = build_qa_agent()
        answer = qa_agent.run(user_query)
        st.success("✅ Answer:")
        st.write(answer)
