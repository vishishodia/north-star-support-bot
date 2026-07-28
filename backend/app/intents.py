from enum import Enum


class Intent(str, Enum):
    GREETING = "GREETING"
    ORDER_TRACKING = "ORDER_TRACKING"
    RETURNS = "RETURNS"
    SHIPPING = "SHIPPING"
    RECOMMENDATION = "RECOMMENDATION"
    LIVE_AGENT = "LIVE_AGENT"
    UNKNOWN = "UNKNOWN"


def detect_intent(message: str) -> Intent:

    message = message.lower().strip()

    words = message.split()

    # Greeting
    if any(word in words for word in ["hi", "hello", "hey"]):
        return Intent.GREETING

    if "good morning" in message or "good evening" in message:
        return Intent.GREETING

    # Order Tracking
    if any(word in message for word in ["order", "track", "package", "shipment"]):
        return Intent.ORDER_TRACKING

    # Returns
    if any(word in message for word in ["return", "exchange", "refund"]):
        return Intent.RETURNS

    # Shipping
    if any(word in message for word in ["shipping", "delivery"]):
        return Intent.SHIPPING

    # Recommendation
    if any(word in message for word in ["recommend", "suggest", "looking for", "need gear"]):
        return Intent.RECOMMENDATION

    # Live Agent
    if any(word in message for word in ["agent", "human", "representative"]):
        return Intent.LIVE_AGENT

    return Intent.UNKNOWN