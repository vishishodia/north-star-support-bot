from enum import Enum
import re


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
    if (
        message.startswith("hi")
        or message.startswith("hello")
        or message.startswith("hey")
        or "good morning" in message
        or "good evening" in message
    ):
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