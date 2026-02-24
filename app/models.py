from pydantic import BaseModel, Field
from typing import Literal


class PredictRequest(BaseModel):
    cmc: float = Field(ge=0, le=20, description="Converted mana cost")
    color_identity: list[str] = Field(description="Color identity, e.g. ['W', 'U']")
    type_line: str = Field(description="Card type line, e.g. 'Creature — Human Wizard'")
    rarity: Literal["common", "uncommon", "rare", "mythic"]
    power: str | None = Field(default=None, description="Creature power (None for non-creatures, can be '*')")
    toughness: str | None = Field(default=None, description="Creature toughness (None for non-creatures)")
    keywords: list[str] = Field(default=[], description="Keywords like ['Flying', 'Trample']")
    set_type: str = Field(description="Set type, e.g. 'expansion', 'core', 'commander'")
    oracle_text_length: int = Field(ge=0, description="Length of rules text in characters")
    year_released: int = Field(ge=1993, le=2030, description="Year the card was released")
    is_reprint: bool = False
    is_reserved: bool = False


class PredictResponse(BaseModel):
    predicted_rank: float = Field(description="Predicted EDHREC rank (1-25000, lower = more popular)")
    confidence: Literal["high", "medium", "low"]


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    sources: list[str]
    tools_used: list[str]
