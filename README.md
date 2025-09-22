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

The project is organized into the following files and directories:

| File/Directory      | Description                                                              |
| :------------------ | :----------------------------------------------------------------------- |
| `cli.py`            | The main entry point for the client discovery process.                   |
| `cli_tdd.py`        | A script for refining an existing discovery report with new information. |
| `gemini_client.py`  | Handles all interactions with the Gemini Pro API.                        |
| `history_client.py` | Manages the local JSON history of client interactions.                   |
| `main.py`           | A utility script for testing the PDF extraction and Gemini integration.  |
| `pdf_loader.py`     | Extracts text from PDF files using PyMuPDF.                              |
| `redis_client.py`   | Handles all interactions with the Redis database.                        |
| `slack_client.py`   | A client for sending messages to a Slack channel.                        |
| `telegram_bot.py`   | A bot for sending messages to a Telegram chat.                           |
| `web_search.py`     | Performs web searches using the SerpAPI.                                 |
| `prompts/`          | Contains the system prompt for the Gemini Pro model.                     |
| `respostas/`        | Stores the generated discovery reports in Markdown format.               |
| `history/`          | Stores the JSON logs of each client interaction.                         |
| `docs/`             | Contains internal reference documents in PDF format.                     |
| `.gitignore`        | Specifies which files and directories to ignore in Git.                  |
| `README.md`         | This file, providing an overview of the project.                         |

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

## ✨ Author

Built with ❤️ by Rafael Ielo  
Role: Solution Architect @ OutSystems  
Mission: Close better deals, faster, with less bullshit.

