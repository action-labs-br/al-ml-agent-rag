"""
Magic: The Gathering card popularity predictor.

Trains a regression model on data/mtg_cards.csv and predicts the EDHREC rank
of a card based on its attributes. EDHREC rank measures Commander format
popularity — lower rank = more popular (rank 1 = Sol Ring, the most-played
card in the format).

Start with an EDA of the dataset to understand the features and challenges.
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
        """Load the MTG dataset, preprocess features, and train a regression model.

        Store the trained model and any fitted encoders/scalers as instance
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
