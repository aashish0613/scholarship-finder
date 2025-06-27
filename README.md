# 🎓 Scholarship Finder

A smart, AI-powered platform that helps students discover and match with scholarships based on their profile, academic background, and eligibility — powered by LangChain, LLaMA3 (via Ollama), and a clean React + Tailwind frontend.

---

## 🚀 Features

- 🔍 Search scholarships using natural language
- 🎯 Matches based on eligibility, category, and academic level
- 🧠 Uses LLaMA3 + LangChain for intelligent retrieval
- 🕸️ Auto-scraped and updated scholarship data
- 🌐 Modern UI using React + Vite + Tailwind CSS



## 🛠️ Tech Stack

| Frontend | Backend | AI/Infra        |
|----------|---------|-----------------|
| React    | FastAPI / Node.js | LLaMA3 via Ollama |
| Vite     | LangChain | Vector Store (e.g., Chroma) |
| Tailwind CSS | Web Scraping | RAG (Retrieval-Augmented Generation) |

---

## 📦 Installation

### Prerequisites

- Node.js & npm
- Python (3.10+)
- Git
- Ollama installed locally
- LangChain, Chroma, etc.

### Clone the repo

```bash
git clone https://github.com/aashish0613/scholarship-finder.git
cd scholarship-finder
```

### Frontend setup

```bash
cd frontend
npm install
npm run dev
```

### Backend setup

```bash
cd backend
pip install -r requirements.txt
python app.py  # or FastAPI/Uvicorn
```

---

## 🤖 AI Setup (Optional)

If you're using LLaMA3 via Ollama:

```bash
ollama run llama3
```

> Make sure your LangChain backend is connected to this locally running LLM.

---

## 📁 Folder Structure

```
scholarship-finder/
├── frontend/           # React + Vite app
│   ├── src/
│   └── ...
├── backend/            # API + RAG system
│   └── ...
├── data/               # Ingested or raw scholarship data
└── README.md
```

---








## 📬 Contact

**Aashish Thakur**  
📍 Sirmour, Himachal Pradesh, India  
📧 [thakuraashish6636@gmail.com](mailto:thakuraashish6636@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/aashish-thakur-11a72025a) | [GitHub](https://github.com/aashish0613)

---

## ⭐ Star This Project

If you find this helpful, please consider starring ⭐ the repo to show your support!