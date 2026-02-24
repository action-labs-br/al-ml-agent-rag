"""
Magic: The Gathering card popularity predictor.

Trains a regression model on data/mtg_cards.csv and predicts the EDHREC rank
of a card based on its attributes. EDHREC rank measures Commander format
popularity — lower rank = more popular (rank 1 = Sol Ring, the most-played
card in the format).

Dataset overview:
    ~10,000 rows, 18 columns (12 input features + 6 derived/target columns).

Key challenges:
    1. Missing power/toughness — ~46% of rows have null power and toughness
       because non-creature cards (instants, sorceries, enchantments, etc.)
       don't have these stats. Your pipeline must handle this gracefully.
    2. "*" in power/toughness — some creatures have variable power/toughness
       (e.g., Tarmogoyf's "*/*+1"). Decide how to encode these.
    3. card_age_days is the dominant feature — newer cards tend to have higher
       (worse) EDHREC ranks because they haven't been adopted yet. Be careful
       not to let this single feature dominate the model to the exclusion of
       other useful signals.
    4. Comma-separated list columns — color_identity and keywords are stored
       as comma-separated strings (e.g., "W,U,B" or "Flying,Trample"). You'll
       need to parse and encode these (one-hot, multi-label, count, etc.).
    5. edhrec_rank (the target) is right-skewed — most cards cluster at high
       ranks (unpopular), while staples have very low ranks. Consider log
       transforms or other strategies.

Suggested approach:
    - Load CSV with pandas
    - Handle missing values (especially power/toughness for non-creatures)
    - Encode categorical features (color_identity, type_line, rarity, set_type)
    - Parse and encode list features (color_identity, keywords)
    - Engineer features (num_colors, is_creature, is_legendary are already provided)
    - Train a regression model (scikit-learn, XGBoost, LightGBM, etc.)
    - The predict() method should return (predicted_rank, confidence)
"""


class CardPopularityPredictor:
    """Predicts EDHREC rank for Magic: The Gathering cards.

    Usage:
        predictor = CardPopularityPredictor()
        predictor.train("data/mtg_cards.csv")
        rank, confidence = predictor.predict(
            cmc=3.0, color_identity=["U"], type_line="Instant",
            rarity="uncommon", power=None, toughness=None,
            keywords=[], set_type="expansion", oracle_text_length=80,
            year_released=2022, is_reprint=False, is_reserved=False,
        )
    """

    def train(self, csv_path: str = "data/mtg_cards.csv") -> None:
        """Load the MTG dataset, preprocess features, and train the model.

        Steps to implement:
            1. Load CSV with pandas
            2. Handle missing values — power/toughness are NaN for ~46% of
               cards (non-creatures). Decide on imputation or indicator strategy.
            3. Parse comma-separated columns: color_identity ("W,U,B") and
               keywords ("Flying,Trample") into usable features.
            4. Encode categoricals: rarity, set_type, type_line (or extract
               super/sub types from the type_line string).
            5. Handle "*" in power/toughness (e.g., treat as NaN, 0, or a
               separate indicator).
            6. Split into train/validation sets.
            7. Train a regression model targeting edhrec_rank.
            8. Store the trained model and any fitted encoders as instance
               attributes for use in predict().

        Args:
            csv_path: Path to the MTG cards CSV file.
        """
        raise NotImplementedError

    def predict(
        self,
        cmc: float,
        color_identity: list[str],
        type_line: str,
        rarity: str,
        power: str | None,
        toughness: str | None,
        keywords: list[str],
        set_type: str,
        oracle_text_length: int,
        year_released: int,
        is_reprint: bool,
        is_reserved: bool,
    ) -> tuple[float, str]:
        """Predict EDHREC rank and confidence for a single card.

        Args:
            cmc: Converted mana cost (0-20).
            color_identity: List of color letters, e.g. ["W", "U"].
            type_line: Full type line, e.g. "Legendary Creature — Elf Druid".
            rarity: One of "common", "uncommon", "rare", "mythic".
            power: Creature power as string (None for non-creatures, "*" possible).
            toughness: Creature toughness as string (None for non-creatures).
            keywords: Keyword abilities, e.g. ["Flying", "Trample"].
            set_type: Set type, e.g. "expansion", "core", "commander".
            oracle_text_length: Character length of the card's rules text.
            year_released: Year the card was printed (1993-2030).
            is_reprint: Whether this printing is a reprint.
            is_reserved: Whether the card is on the Reserved List.

        Returns:
            A tuple of (predicted_rank, confidence) where:
            - predicted_rank is a float (1-25000, lower = more popular)
            - confidence is "high", "medium", or "low" based on how well
              the input matches training data distribution and model certainty.
        """
        raise NotImplementedError
