# Astolfo 🤖 – Client Discovery Assistant

Astolfo is your AI-powered assistant designed to support client discovery, research, and pre-sales analysis — tailored for **OutSystems** sales professionals.

---

## 🧩 Features – v1

- 🔍 **Discovery Mode**  
  Input a company name and Astolfo will:
  - Search relevant web sources using SerpAPI
  - Include internal references from pre-defined templates
  - Build a rich prompt and ask Gemini Pro (1.5 Flash) for insight
  - Return a structured report (markdown)
  - Save results locally (`respostas/`) and on Redis

- ✏️ **Refine Mode** (`cli_tdd.py`)  
  Input additional notes or meeting details and Astolfo:
  - Retrieves the latest version of the response
  - Sends a refined prompt to Gemini with new context
  - Updates Redis and saves the new version in `respostas/`

- 📦 **Storage**
  - Local `.md` archive per client
  - JSON snapshots in `history/`
  - Redis store for quick retrieval and version control

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/seu-usuario/astolfo.git
cd astolfo

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GOOGLE_API_KEY="your-gemini-api-key"
export SERPAPI_API_KEY="your-serpapi-api-key"

# Start Discovery Mode
python cli.py

# Refine after a meeting
python cli_tdd.py
```

---

## 🧠 Prompt Structure

Astolfo uses a system prompt + web results + internal guidance to generate structured answers:
- Overview
- Investment Reports
- How OutSystems Can Help
- Technologies
- CBI
- Pain Points
- Relevant News
- Scope Summary
- Risks
- Sources Used

---

## 🗃 Project Structure

```
astolfo/
├── cli.py                  → Main discovery script
├── cli_tdd.py              → Refine response after a meeting
├── gemini_client.py        → Gemini API logic
├── redis_client.py         → Redis store/retrieve helpers
├── web_search.py           → SerpAPI-based search module
├── prompts/
│   └── system_prompt.py    → Static system prompt used for every request
├── respostas/              → Markdown responses (by client)
├── history/                → JSON logs of each run
├── docs/                   → Internal reference PDFs
├── .env / .gitignore       → Environment & git hygiene
```

---

## 📈 Evolution Plan – v2

| Feature | Description |
|--------|-------------|
| ✅ History v1 | Saved in Redis + local JSON |
| ✅ Multi-step prompt (refine) | Add context over time |
| 🚧 Slack integration | Receive & send requests via Slack |
| 🚧 Telegram Bot | Allow inline queries or refinements |
| 🚧 Contextual RAG | Use Redis to store + query vectorized chunks |
| 🔜 Streamlit Dashboard | Searchable GUI to browse responses, logs, refine |
| 🔜 PDF/Slide Export | One-click export of response as PowerPoint or PDF |
| 🔜 Audio Interface | Receive voice notes, transcribe, refine |
| 🔜 Shared Multi-Client Mode | Allow multiple users to use the same instance |

---

## ☁️ How to Push to GitHub

1. Create your GitHub repo: `https://github.com/usuario/astolfo`
2. In terminal:

```bash
git init
git remote add origin https://github.com/usuario/astolfo.git
git add .
git commit -m "Initial version of Astolfo (v1)"
git branch -M main
git push -u origin main
```

---

## ✨ Author

Built with ❤️ by Rafael Ielo  
Role: Solution Architect @ OutSystems  
Mission: Close better deals, faster, with less bullshit.

