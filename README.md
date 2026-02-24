# Technical Challenge — AI/ML Engineer

## Scenario

**SpellForge** builds intelligent tools for the Magic: The Gathering community. Their flagship product is a Commander format analytics platform that predicts card popularity using EDHREC data and answers strategy questions using a knowledge base of MTG concepts.

The engineering team needs you to build the backend: a prediction endpoint for EDHREC rank estimation and an intelligent chat agent, exposed via API.

---

## Why Magic: The Gathering Commander matters

Commander is the most popular constructed format in Magic: The Gathering, accounting for over **50% of all Magic play sessions** worldwide. It's a 100-card singleton format where a legendary creature serves as your "commander" and restricts which cards you can include based on color identity. The format supports 4 players, starts at 40 life, and creates rich strategic decisions.

**EDHREC** (edhrec.com) is the community's primary analytics platform, tracking over **2 million decklists** to rank every card by popularity. Understanding what makes a card popular — its cost, color identity, type, rarity, keywords, and release timing — is the prediction challenge.

## About the data

The dataset contains **~10,000 Magic: The Gathering cards** with attributes relevant to Commander popularity. The prediction target is **`edhrec_rank`** — a numerical ranking where lower = more popular (rank 1 = Sol Ring, the most-played card in the format).

| Feature | What it means |
|---------|---------------|
| `cmc` | Converted mana cost — total mana to cast the spell (0-16) |
| `color_identity` | Colors the card belongs to, e.g. "W,U,B" (comma-separated) |
| `type_line` | Full card type, e.g. "Legendary Creature — Human Wizard" |
| `rarity` | common, uncommon, rare, mythic |
| `power` / `toughness` | Creature stats (null for non-creatures, can be "*") |
| `keywords` | Keyword abilities, e.g. "Flying,Trample" (comma-separated) |
| `set_type` | Product type: expansion, commander, masters, core, etc. |
| `oracle_text_length` | Character length of the card's rules text |
| `year_released` | Year the card was printed (1993-2024) |
| `is_reprint` | Whether this printing is a reprint |
| `is_reserved` | Whether the card is on the Reserved List (can never be reprinted) |
| `num_colors` | Derived: count of colors in color_identity (0 = colorless) |
| `is_creature` | Derived: whether the card is a creature |
| `is_legendary` | Derived: whether the card has the Legendary supertype |
| `card_age_days` | Derived: days since release (dominant predictor — see challenges) |

### Key challenges

1. **46% missing power/toughness** — Non-creature cards (instants, sorceries, enchantments, artifacts, planeswalkers, lands) have no power/toughness. Your pipeline must handle these nulls.
2. **Temporal confound** — `card_age_days` is the single strongest predictor because newer cards have inflated EDHREC ranks due to recency bias. A naive model may over-rely on this feature.
3. **"*" in power/toughness** — Some creatures have variable stats (e.g., Tarmogoyf). Decide how to encode these.
4. **Comma-separated lists** — `color_identity` and `keywords` are stored as comma-separated strings that need parsing and encoding.
5. **Right-skewed target** — Most cards cluster at high ranks (unpopular). Consider log transforms or other strategies.

---

## What you need to build

Two endpoints in `app/main.py` (`/health` is already done). Schemas are in `app/models.py`.

### `POST /predict`

Predict the EDHREC rank (popularity) for a Magic: The Gathering card based on its attributes.

**Request:**
```json
{
  "cmc": 5.0,
  "color_identity": ["W", "U", "B"],
  "type_line": "Legendary Creature — Human Wizard",
  "rarity": "mythic",
  "power": "4",
  "toughness": "4",
  "keywords": ["Flying"],
  "set_type": "expansion",
  "oracle_text_length": 200,
  "year_released": 2020,
  "is_reprint": false,
  "is_reserved": false
}
```

**Response:**
```json
{
  "predicted_rank": 1250.0,
  "confidence": "high"
}
```

### `POST /chat`

Natural language question → agent response. The agent decides between searching documents (RAG) or querying the prediction model (tool calling).

**Request:**
```json
{
  "message": "How popular would a 3-mana blue instant be in Commander?"
}
```

**Response (prediction query):**
```json
{
  "response": "Based on the predictive model, a 3-mana blue instant would likely have an EDHREC rank around 8500, placing it in the moderately popular range.",
  "sources": [],
  "tools_used": ["predict_card_popularity"]
}
```

**Request:**
```json
{
  "message": "What is the color pie in Magic: The Gathering?"
}
```

**Response (document search):**
```json
{
  "response": "The color pie is Magic's core design philosophy, built around five colors of mana — White (W), Blue (U), Black (B), Red (R), and Green (G), collectively called WUBRG...",
  "sources": ["color_pie.md"],
  "tools_used": ["search_documents"]
}
```

---

## Provided files

Stubs with a defined interface. You may add files and dependencies, but keep the existing property names — the interface is the contract.

| File | Description |
|------|-------------|
| `app/main.py` | FastAPI endpoints — `/health` (done), `/predict` and `/chat` (to implement) |
| `app/models.py` | Pydantic request/response schemas (with validation) |
| `app/config.py` | Environment variables (API key, model name) |
| `app/predictor.py` | `CardPopularityPredictor` — `train()` and `predict()` to implement |
| `app/agent.py` | `SpellForgeAgent` — `process_message()` to implement |
| `data/mtg_cards.csv` | ~10,000 rows of MTG card data (Kaggle / Scryfall). Target: `edhrec_rank`. Start with an EDA. |
| `data/docs/` | 6 markdown documents — knowledge base for the RAG agent |

---

## Technical requirements

- **Python 3.11+**
- **FastAPI** for the API
- **LLM via OpenRouter** — create a free account at [openrouter.ai](https://openrouter.ai). The default model (`meta-llama/llama-3.3-70b-instruct:free`) is free. You may use any LLM provider — justify your choice in your README.
- **Docker** — `docker compose up` must start the entire application on port **8000**
- **ML framework**: free choice (scikit-learn, XGBoost, LightGBM, etc.)
- **RAG framework**: free choice (LangChain, LangGraph, CrewAI, LlamaIndex, etc.)

---

## Getting started

1. **Download the contents** of this repository and create a new public repository on GitHub
2. **Set up the environment** — copy `.env.example` to `.env` and fill in your API key:
   ```bash
   cp .env.example .env
   ```
3. **Implement the solution** — fill in the stubs in `app/`
4. **Make sure Docker works** — `docker compose up` must start the complete application
5. **Test the 3 endpoints** — `/health`, `/predict`, and `/chat`

---

## Evaluation

We evaluate correctness, code quality, and technical decisions. Include in your README the choices you made and why.

No hosting required. Publish to a public GitHub repository and share the link.
