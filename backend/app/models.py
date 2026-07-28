from enum import Enum
from typing import Optional
from pydantic import BaseModel


class ConversationState(str, Enum):
    MAIN_MENU = "MAIN_MENU"

    AWAITING_ORDER = "AWAITING_ORDER"

    RETURNS = "RETURNS"
    SHIPPING = "SHIPPING"

    RECOMMENDATION_ACTIVITY = "RECOMMENDATION_ACTIVITY"
    RECOMMENDATION_WEATHER = "RECOMMENDATION_WEATHER"
    RECOMMENDATION_BUDGET = "RECOMMENDATION_BUDGET"

    LIVE_AGENT = "LIVE_AGENT"


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    reply: str
    state: ConversationState
    quick_replies: Optional[list[str]] = None


class ResetResponse(BaseModel):
    session_id: str