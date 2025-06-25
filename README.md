# 🤖 AI Research Paper Summarizer

This is a web application that uses OpenAI’s GPT-4o model to summarize research papers directly from URLs. It’s built using Flask and provides a clean, responsive UI with markdown rendering, dark mode, PDF export, and optional email input for future use.

---

## ✨ Features

- 🔗 Accepts URLs of publicly accessible research papers
- 🧠 Summarizes using OpenAI GPT-4o (via API)
- 📄 Shows:
  - A comprehensive summary
  - Key contributions
  - Comparison with related techniques
  - Future research ideas
- 🌗 Toggle between light and dark modes
- 📥 Download summary as PDF


---

## 🛠 Built With

- Python 3.8+
- Flask
- OpenAI Python SDK
- fpdf
- BeautifulSoup4
- HTML + CSS (GitHub-style markdown)

---

## 🧑‍💻 How to Run It Locally

### 1. Clone the Repository

```bash
git clone https://github.com/ruchirnamjoshi/Research-Paper-Summariser
cd Research-Paper-Summariser
```

### 2. Set Up Environment

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXXXXXXXXXXXXX
```

### 3. Run the Flask App

```bash
python app.py
```

Open your browser and visit:
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
research-summarizer/
├── app.py                 # Main Flask app
├── summarizer.py          # Logic to fetch + summarize paper
├── templates/
│   └── index.html         # Frontend HTML template
├── static/
│   └── style.css (opt.)   # Optional CSS for extra theming
├── requirements.txt       # Python dependencies
└── .env                   # OpenAI API key (not committed)
```

---

## 🔐 Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (starts with `sk-proj-...`)

---

## 💡 Example Use Case

Paste a URL like this:
```
https://arxiv.org/abs/2406.12345
```
Click **Generate Summary**, wait a few seconds, and see a clean markdown-rendered summary. Optionally download it as a PDF.

---

## 🔧 Future Improvements

- [ ] Email delivery of summaries
- [ ] Upload and summarize PDF files
- [ ] Save user history (session-based)
- [ ] Add citation generation support

---

## 🤝 Contributing

Found a bug or have an idea? Open an issue or submit a pull request!

---

## 🙌 Acknowledgments

- [OpenAI](https://openai.com/)
- [GitHub Markdown CSS](https://github.com/sindresorhus/github-markdown-css)
