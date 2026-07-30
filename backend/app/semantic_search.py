from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from app.intents import Intent

# Load model once when the server starts
model = SentenceTransformer("all-MiniLM-L6-v2")

INTENT_EXAMPLES = {
    Intent.ORDER_TRACKING: [
        "track my order",
        "where is my order",
        "where is my package",
        "track package",
        "order status",
        "shipment status",
        "has my package arrived",
        "check my order"
    ],

    Intent.RETURNS: [
        "return an item",
        "refund",
        "exchange product",
        "return policy",
        "send my order back"
    ],

    Intent.SHIPPING: [
        "shipping information",
        "delivery options",
        "shipping cost",
        "how long does shipping take"
    ],

    Intent.RECOMMENDATION: [
        "recommend a product",
        "help me choose",
        "suggest something",
        "what should i buy"
    ],

    Intent.LIVE_AGENT: [
        "talk to a person",
        "human support",
        "customer representative",
        "live agent"
    ],

    Intent.GREETING: [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good evening"
    ]
}

example_sentences = []
example_intents = []

for intent, examples in INTENT_EXAMPLES.items():
    for sentence in examples:
        example_sentences.append(sentence)
        example_intents.append(intent)

example_embeddings = model.encode(example_sentences)

def semantic_intent(message: str):

    embedding = model.encode([message])

    scores = cosine_similarity(
        embedding,
        example_embeddings
    )[0]

    best_index = scores.argmax()

    if scores[best_index] < 0.50:
        return Intent.UNKNOWN

    return example_intents[best_index]

def detect_intent(message: str):
    """
    Main entry point for intent detection.
    """
    return semantic_intent(message.strip().lower())