from enum import Enum
import re

from rapidfuzz import fuzz, process


class Intent(str, Enum):
    GREETING = "GREETING"
    ORDER_TRACKING = "ORDER_TRACKING"
    RETURNS = "RETURNS"
    SHIPPING = "SHIPPING"
    RECOMMENDATION = "RECOMMENDATION"
    LIVE_AGENT = "LIVE_AGENT"
    UNKNOWN = "UNKNOWN"


# Shared keyword source of truth, also used by the fuzzy matcher below.
GREETING_WORDS = ["hi", "hello", "hey"]
GREETING_PHRASES = ["good morning", "good evening"]

INTENT_KEYWORDS = {
    Intent.ORDER_TRACKING: ["order", "track", "package", "shipment"],
    Intent.RETURNS: ["return", "exchange", "refund"],
    Intent.SHIPPING: ["shipping", "delivery"],
    Intent.RECOMMENDATION: ["recommend", "suggest", "looking for", "need gear"],
    Intent.LIVE_AGENT: ["agent", "human", "representative"],
}


def fuzzy_intent(message: str, threshold: int = 82) -> Intent:
    """
    Typo-tolerant fallback. Catches misspellings like "shiping",
    "retrun", "recomend", "hllo" that exact keyword matching misses,
    without being loose enough to start guessing on genuinely novel
    phrasing (that's what semantic_intent is for).
    """

    if not message:
        return Intent.UNKNOWN

    term_to_intent = {}

    for word in GREETING_WORDS:
        term_to_intent[word] = Intent.GREETING
    for phrase in GREETING_PHRASES:
        term_to_intent[phrase] = Intent.GREETING
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            term_to_intent[keyword] = intent

    all_terms = list(term_to_intent.keys())

    best_intent = Intent.UNKNOWN
    best_score = 0

    # Check the full message (catches phrases like "good morning")
    # and each individual word (catches single-word typos).
    candidates = [message] + message.split()

    for candidate in candidates:
        match = process.extractOne(candidate, all_terms, scorer=fuzz.ratio)

        if match is None:
            continue

        term, score, _ = match

        if score > best_score:
            best_score = score
            best_intent = term_to_intent[term]

    if best_score >= threshold:
        return best_intent

    return Intent.UNKNOWN


def detect_intent(message: str):

    from app.semantic_search import semantic_intent

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

    # Typo-tolerant fallback (catches misspelled keywords before
    # falling through to the slower semantic embedding match)
    fuzzy_result = fuzzy_intent(message)
    if fuzzy_result != Intent.UNKNOWN:
        return fuzzy_result

    # Semantic fallback
    return semantic_intent(message)


def normalize_activity(message: str):
    message = message.lower()

    if any(word in message for word in [
        "hiking", "hike", "trek", "trekking", "mountain", "trail"
    ]):
        return "Hiking"

    if any(word in message for word in [
        "camping", "camp", "tent", "outdoors", "outdoor"
    ]):
        return "Camping"

    if any(word in message for word in [
        "running", "run", "runner", "jog", "jogging", "marathon"
    ]):
        return "Running"

    return None


def normalize_weather(message: str):
    message = message.lower()

    if any(word in message for word in [
        "cold", "snow", "snowing", "winter", "freezing",
        "freeze", "icy", "ice", "chilly"
    ]):
        return "Cold"

    if any(word in message for word in [
        "rain", "rainy", "storm", "stormy",
        "wet", "drizzle", "showers"
    ]):
        return "Rainy"

    if any(word in message for word in [
        "mild", "warm", "pleasant", "nice",
        "sunny", "clear", "comfortable",
        "cool", "spring", "autumn", "fall"
    ]):
        return "Mild"

    return None

def normalize_budget(message: str):

    message = message.lower().strip()

    # Under $100
    if any(word in message for word in [
        "cheap",
        "budget",
        "under 100",
        "less than 100",
        "below 100",
        "affordable",
        "low cost"
    ]):
        return "Under $100"

    # $100-$250
    if any(word in message for word in [
        "premium",
        "expensive",
        "under 250",
        "below 250",
        "less than 250",
        "100-250",
        "$100-$250",
        "mid range"
    ]):
        return "$100-$250"

    # Handle numbers like "200 dollars", "$180", "150"
    numbers = re.findall(r"\d+", message)

    if numbers:
        value = int(numbers[0])

        if value < 100:
            return "Under $100"

        if 100 <= value <= 250:
            return "$100-$250"

    return None