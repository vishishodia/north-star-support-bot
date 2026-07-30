# North Star Support Bot 🏔️

A customer support chatbot for an outdoor apparel and camping gear e-commerce brand. Built with FastAPI and semantic search (Sentence Transformers) — no LLM or API key required.

## Features

- 📦 **Order Tracking** – Track orders using mock order numbers (111, 222, 333)
- ↩️ **Returns & Exchanges** – 30-day return policy with exchange support
- 🚚 **Shipping Information** – Standard and expedited shipping options
- 🎒 **Smart Product Recommendations** – Personalized recommendations based on activity, weather, and budget
- 💬 **Natural Language Understanding** – Understands conversational inputs such as:
  - "I'm going trekking" → Hiking
  - "It will snow" → Cold weather
  - "Need something cheap" → Under $100
- 👨‍💼 **Human Agent Handoff** – Simulated live agent mode that remains active until the user selects **Main Menu**
- 🔄 **Conversation State Management** – Maintains context across multi-step conversations
- ❓ **Fallback Handling** – Friendly responses for unsupported queries with quick-reply suggestions

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


## Recent Improvements

Based on reviewer feedback, the chatbot now includes:

- Enhanced natural language understanding for activities, weather, and budgets
- Complete recommendation coverage for all activity × weather × budget combinations
- Persistent live agent mode until the user explicitly returns to the Main Menu
- Improved conversation flow while tracking orders
- Better quick-reply support throughout the chatbot
