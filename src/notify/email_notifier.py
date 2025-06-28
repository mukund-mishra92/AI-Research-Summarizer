import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from storage.database import get_recent_articles

load_dotenv()

def notify_user():
    articles = get_recent_articles(limit=10)  # 👈 get latest 10 articles
    if not articles:
        print("ℹ️ No new articles to email.")
        return

    # Format email
    body = "🧠 *Recent AI Articles Digest*\n\n"
    for a in articles:
        body += f"📘 {a['title']} ({a['source']})\n"
        body += f"📝 {a['summary']}\n"
        body += f"🕒 {a['published']}\n\n"

    send_email("🧠 Daily AI Research Digest", body)

def send_email(subject: str, body: str):
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)

def send_email_summary(to_email, subject, body):
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = to_email

    with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("EMAIL_FROM"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)

