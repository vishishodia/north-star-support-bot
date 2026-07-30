# North Star Support Bot 🏔️

A customer support chatbot for an outdoor apparel and camping gear e-commerce brand. Built with FastAPI and semantic search (Sentence Transformers) — no LLM or API key required.

## Features

- 📦 **Order Tracking** – Track orders using mock order numbers (111, 222, 333)
- ↩️ **Returns & Exchanges** – 30-day return policy with exchange support
- 🚚 **Shipping Information** – Standard and expedited shipping options
- 🎒 **Smart Product Recommendations** – Personalized recommendations based on activity, weather, and budget
- 💬 **Natural Language Understanding** – Three-layer intent detection:
  - **Keyword matching** for clear, direct phrasing ("track my order")
  - **Typo tolerance** (RapidFuzz) for misspellings ("shiping", "retrun", "recomend")
  - **Semantic matching** (Sentence Transformers) for paraphrased/novel input ("has my package arrived", "help me choose some gear")
- 👨‍💼 **Human Agent Handoff** – Simulated live agent mode that remains active until the user selects **Main Menu**
- 🔄 **Conversation State Management** – Maintains context across multi-step conversations
- ❓ **Fallback Handling** – Friendly responses for unsupported queries with quick-reply suggestions

## Tech Stack

- **Backend:** FastAPI, Pydantic
- **NLP:** Sentence Transformers (`all-MiniLM-L6-v2`), scikit-learn (cosine similarity), RapidFuzz (typo tolerance)
- **Frontend:** HTML/CSS/JS
- **No external services:** No OpenAI/API keys, no deployment required — fully testable locally

## Project Structure

The backend is organized as a request → route → conversation logic → NLP pipeline:

```
north-star-support-bot/
├── backend/
│   └── app/
│       ├── main.py             # FastAPI app entrypoint
│       ├── routes.py           # API endpoints (/chat, /reset, /health)
│       │
│       ├── chatbot.py          # Core conversation state machine
│       ├── session.py          # In-memory session/state management
│       │
│       ├── intents.py          # Intent detection: keyword + typo-tolerant (fuzzy) matching
│       ├── semantic_search.py  # Intent detection: embedding-based semantic matching
│       │
│       ├── models.py           # Pydantic request/response models
│       ├── data.py             # Mock orders, return policy, shipping info, recommendations
│       └── utils.py            # Text normalization helpers
│
├── frontend/
│   └── index.html              # Chat UI (single-file HTML/CSS/JS)
│
├── requirements.txt            # Python dependencies
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.10+

### Installation

```bash
git clone https://github.com/vishishodia/north-star-support-bot.git
cd north-star-support-bot

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Run the backend

```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

> **Note:** The first run downloads the `all-MiniLM-L6-v2` embedding model from Hugging Face, so an internet connection is required at least once. Subsequent runs use the local cache.

### Run the frontend

Open `frontend/index.html` in your browser (or serve it with a simple static server).

## Testing the Chatbot

Try these inputs to see the different flows:

| User Input                             | Expected Result          |
| -------------------------------------- | ------------------------ |
| hello                                  | Greeting                 |
| track my order                         | Prompts for order number |
| 111                                    | Shipped                  |
| 222                                    | Processing               |
| 333                                    | Delivered                |
| 999                                    | Invalid order            |
| returns                                | Return policy            |
| shipping                               | Shipping options         |
| recommendations                        | Recommendation flow      |
| I'm going trekking                     | Hiking                   |
| It will snow                           | Cold                     |
| Need something cheap                   | Under $100               |
| Camping → Pleasant → Under 250 dollars | Camping recommendations  |
| live agent                             | Human handoff            |
| Main Menu                              | Returns to chatbot       |
| I like pizza                           | Fallback response        |

### Typo tolerance

The bot understands common misspellings without needing exact keywords:

| User Input            | Expected Result      |
| ---------------------- | --------------------- |
| shiping info please     | Shipping options       |
| retrun policy           | Return policy          |
| recomend something      | Recommendation flow    |
| hllo there              | Greeting                |

### Semantic understanding

Paraphrased requests with no matching keyword are still routed correctly:

| User Input                  | Expected Result     |
| ----------------------------- | --------------------- |
| has my package arrived yet     | Order Tracking          |
| help me choose some gear       | Recommendation flow     |
| talk to a real person          | Human handoff            |
| what's your return window      | Return policy             |

