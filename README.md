# AI Research Summarizer 🤖📚

An intelligent system that automatically fetches, summarizes, and delivers AI research papers and news using state-of-the-art language models.

## Features 🌟

- **Multi-source Fetching**: Retrieves content from:
  - arXiv papers 📑
  - News articles 📰
  - RSS feeds 📡
  
- **Smart Summarization**: 
  - Uses HuggingFace's DistilBART model (free, runs locally)
  - Pre-trained on CNN news articles for high-quality summaries
  - Maintains context and key findings
  - Configurable summary length
  - No API keys or costs required

- **Multiple Notification Channels**:
  - Email digests 📧
  - Telegram updates 📱
  - Web interface 🌐

- **Scheduled Updates**:
  - Automated daily fetching
  - Customizable scheduling
  - Background processing

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/mukund-mishra92/AI-Research-Summarizer.git
cd AI-Research-Summarizer
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Note: If faiss-cpu installation fails, use:
```bash
pip install faiss-cpu --prefer-binary
```

## Configuration ⚙️

1. Create a `.env` file in the `src` directory with:
```env
# Email Configuration
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=recipient@email.com

# Telegram Configuration (Optional)
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

2. Customize `config.yml` for source settings:
```yaml
arxiv:
  query: "artificial intelligence"
  max_results: 10
```

## Usage 💡

1. Run the main script:
```bash
python src/main.py
```

2. Start the web interface:
```bash
streamlit run src/ui/app.py
```

3. Schedule automated runs:
```bash
python src/scheduler.py
```

## Project Structure 📁

```
src/
├── agent/          # RAG Chain implementation
├── components/     # Core components
├── fetch/         # Source fetchers
├── notify/        # Notification systems
├── storage/       # Database management
├── summarize/     # Text summarization
└── ui/            # Web interface
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License 📄

MIT License - See LICENSE file for details
