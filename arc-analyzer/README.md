# 🛡️ ARC Analyzer – AI-Powered Risk & Compliance Tool

![GitHub Repo Size](https://img.shields.io/github/repo-size/yourusername/arc-analyzer)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/arc-analyzer)
![License](https://img.shields.io/github/license/yourusername/arc-analyzer)
![OpenAI Powered](https://img.shields.io/badge/AI-GPT4-blueviolet)

> Quickly extract, summarize, and risk-map controls from compliance documents using GPT-4.

---

## 🚀 Features

- 📄 Upload PDF or DOCX compliance documents
- 🤖 GPT-powered control summarization and CIA risk mapping
- 📋 Export results to CSV
- ⚡ Built with Streamlit for instant deployment

---

## 🧪 Demo

[![Watch the demo](https://img.shields.io/badge/Demo-YouTube-red)](https://your-youtube-link.com)

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/arc-analyzer.git
cd arc-analyzer
```

### 2. Create a `.env` File

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Locally

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
arc-analyzer/
├── app.py           # Streamlit app logic
├── parser.py        # PDF/DOCX extraction
├── prompts.py       # GPT prompt templates
├── utils.py         # GPT call + export
├── .env             # API key (excluded from git)
└── README.md
```

---

## 📤 Deployment

Use [Streamlit Cloud](https://streamlit.io/cloud) to deploy in 60 seconds!

---

## 📄 License

This project is under the [MIT License](LICENSE).

---

## 🤝 Contributing

PRs welcome! Please open an issue to discuss before submitting major changes.

---

## 🙏 Acknowledgements

- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [OpenAI API](https://platform.openai.com/)
