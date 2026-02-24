"""
RAG agent with tool calling for SpellForge MTG.

Builds a knowledge base from data/docs/ (6 markdown files) and provides
an intelligent agent that decides between two actions:

1. search_documents — semantic search in the knowledge base for questions
   about Magic: The Gathering strategy, card evaluation, Commander format
   rules, the color pie, mana curves, set design, rarity, and the EDHREC
   metagame. Returns relevant text chunks and source filenames.

2. predict_card_popularity — extracts card attributes from natural language
   and calls the CardPopularityPredictor for EDHREC rank estimation.

Knowledge base files (data/docs/):
    - commander_format.md      — Commander rules, singleton, color identity, commander tax
    - color_pie.md             — WUBRG colors, color pairs, three-color combos
    - mana_curve_and_evaluation.md — CMC, mana curve, ramp, BREAD, quadrant theory
    - card_types_and_strategy.md   — Creatures, instants, sorceries, enchantments, artifacts, lands
    - set_design_and_rarity.md     — Rarity, set types, Reserved List, reprints, power creep
    - edhrec_and_metagame.md       — EDHREC.com, rank system, staples, metagame shifts

Suggested approach:
    - Chunk the 6 markdown documents and embed into a vector store
      (ChromaDB, FAISS, Pinecone, etc.)
    - Define two tools for the agent: search_documents and predict_card_popularity
    - Use an LLM via OpenRouter (see config.py) to orchestrate tool selection
    - You may use any LLM provider — just update config.py and .env accordingly
    - Framework choice is yours: LangChain, LangGraph, LlamaIndex, CrewAI, or custom

The process_message() method should return a dict with:
    - "response": the agent's text response
    - "sources": list of source filenames used (e.g., ["color_pie.md"])
    - "tools_used": list of tool names used (e.g., ["predict_card_popularity"],
      ["search_documents"], or ["predict_card_popularity", "search_documents"])
"""

from app.predictor import CardPopularityPredictor


class SpellForgeAgent:
    """RAG agent for Magic: The Gathering questions and card popularity prediction.

    Combines semantic search over MTG knowledge base documents with a trained
    card popularity predictor. The agent uses an LLM to decide which tool(s)
    to invoke based on the user's question.

    Example questions that should trigger search_documents:
        - "What is the color pie in Magic?"
        - "How does commander tax work?"
        - "What makes a card a staple in Commander?"

    Example questions that should trigger predict_card_popularity:
        - "How popular would a 3-mana blue instant with Flying be?"
        - "Predict the EDHREC rank for a mythic legendary creature"

    Example questions that might use both tools:
        - "Why would a low-CMC colorless artifact rank well on EDHREC?"
    """

    def __init__(self, predictor: CardPopularityPredictor):
        self.predictor = predictor
        # TODO: load and chunk documents from data/docs/
        # TODO: embed chunks into a vector store (ChromaDB, FAISS, etc.)
        # TODO: set up LLM client via OpenRouter (see config.py)
        # TODO: define tools and wire up the agent loop

    def process_message(self, message: str) -> dict:
        """Process a user message and return agent response.

        The agent should:
            1. Analyze the user's message to determine intent
            2. Call search_documents if the question is about MTG knowledge
            3. Call predict_card_popularity if the question asks for a rank prediction
            4. Call both tools if the question requires knowledge + prediction
            5. Synthesize the tool outputs into a natural language response

        Args:
            message: The user's natural language question.

        Returns:
            A dict with keys:
            - "response" (str): The agent's answer.
            - "sources" (list[str]): Filenames from data/docs/ that were used.
            - "tools_used" (list[str]): Tool names that were invoked.
        """
        raise NotImplementedError
