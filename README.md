# North Star Support Bot 🏔️

A customer support chatbot for an outdoor apparel and camping gear e-commerce brand. Built with FastAPI and semantic search (Sentence Transformers) — no LLM or API key required.

## Features

- **Order Tracking** — Look up order status by order number (mock data)
- **Returns & Exchanges** — 30-day return policy, unused items, original packaging required
- **Shipping Info** — Standard (3–5 business days) and expedited (1–2 business days) options
- **Product Recommendations** — Guided flow based on activity, weather, and budget
- **Human Handoff** — Simulated live agent transition with fallback to main menu
- **Fallback Handling** — Clear "I didn't understand" response with next-step options
- **Natural language understanding** — Handles phrasing variations (e.g. "where's my package" vs "track my order") using semantic similarity, not just keyword matching

## Tech Stack

- **Backend:** FastAPI, Pydantic
- **NLP:** Sentence Transformers (`all-MiniLM-L6-v2`), scikit-learn (cosine similarity), RapidFuzz (typo tolerance)
- **Frontend:** HTML/CSS/JS
- **No external services:** No OpenAI/API keys, no deployment required — fully testable locally

## Project Structure

\```
north-star-support-bot/
├── backend/
│   └── app/
│       ├── chatbot.py          # Core conversation logic
│       ├── data.py             # Mock orders, return policy, shipping info
│       ├── intents.py          # Intent detection (keyword + fuzzy)
│       ├── semantic_search.py  # Embedding-based intent matching
│       ├── models.py           # Pydantic request/response models
│       ├── routes.py           # API endpoints
│       ├── session.py          # Conversation state management
│       └── main.py             # FastAPI app entrypoint
├── frontend/                   # Chat UI
├── requirements.txt
├── .gitignore
└── README.md
\```

## Getting Started

### Prerequisites
- Python 3.10+

### Installation

\```bash
git clone https://github.com/vishishodia/north-star-support-bot.git
cd north-star-support-bot

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install -r requirements.txt
\```

### Run the backend

\```bash
cd backend
uvicorn app.main:app --reload
\```

The API will be available at `http://localhost:8000`.

### Run the frontend

Open `frontend/index.html` in your browser (or serve it with a simple static server).

## Testing the Chatbot

Try these inputs to see the different flows:

| Input | Expected Behavior |
|---|---|
| `hi` | Greeting + main menu options |
| `track my order` → `111` | Order #111: Shipped, arriving tomorrow |
| `track my order` → `222` | Order #222: Processing, ships in 24 hours |
| `track my order` → `333` | Order #333: Delivered |
| `track my order` → `999` | Invalid order message |
| `returns` | Return policy (30-day, unused, original packaging) |
| `shipping` | Standard vs expedited shipping info |
| `recommend something` | Guided flow: activity → weather → budget → recommendation |
| `talk to a human` | Simulated live agent handoff |
| `asdkfjasdf` | Fallback: "I didn't understand" with options |

## Notes

This project was built as part of the Upwork Talent Accelerator program. It uses only the mock data and business rules specified in the project contract — no live order/payment systems are connected.
