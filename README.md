# 🛡️ ARC Analyzer – AI-Powered Risk & Compliance Tool

ARC Analyzer is a lightweight, AI-driven tool that helps Governance, Risk, and Compliance (GRC) professionals **analyze regulatory frameworks** and **generate control mappings, risk registers, and compliance matrices** automatically from uploaded documents.

---

## 🚀 Features

- 📂 Upload PDF or DOCX documents (e.g., NIST 800-53, HIPAA, ISO 27001)
- 🧠 Uses GPT-4 to:
  - Extract and summarize controls
  - Map controls to risk categories (CIA triad)
  - Auto-generate risk register and compliance matrix
- 📊 Export results as CSV
- 🌐 Web-based UI (Streamlit)

---

## 🎯 Use Cases

- Rapid control identification for audits
- Cross-mapping frameworks
- AI-assisted compliance document review
- GRC program acceleration for startups and enterprises

---

## 🧰 Tech Stack

| Component     | Tool/Library           |
|---------------|------------------------|
| Frontend UI   | Streamlit              |
| Backend       | Python                 |
| AI Model      | OpenAI GPT-4           |
| PDF Parsing   | PyMuPDF / pdfplumber   |
| Export        | pandas, CSV            |
| Deployment    | Streamlit Cloud / Render |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/arc-analyzer.git
cd arc-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
