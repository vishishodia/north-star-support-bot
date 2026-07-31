from app.models import ChatResponse, ConversationState
from app.intents import detect_intent, normalize_activity, normalize_weather, normalize_budget, Intent
from app.data import ORDERS, RETURN_POLICY, SHIPPING_INFO, RECOMMENDATIONS


class ChatBot:

    def process_message(self, session, message):

        # Stay in Live Agent mode until the user requests the Main Menu.
        if session["state"] == ConversationState.LIVE_AGENT:

            if message.lower().strip() in [
                "main menu",
                "menu",
                "back",
                "return",
                "chatbot"
            ]:

                session["state"] = ConversationState.MAIN_MENU

                return ChatResponse(
                    reply=(
                        "Welcome back! 😊\n\n"
                        "You're now chatting with the North Star Support Bot."
                    ),
                    state=ConversationState.MAIN_MENU,
                    quick_replies=[
                        "Track Order",
                        "Returns",
                        "Shipping",
                        "Recommendations",
                        "Live Agent"
                    ]
                )

            return ChatResponse(
                reply=(
                    "👨‍💼 Live Agent:\n\n"
                    "Thanks for your message. A support representative is assisting you.\n\n"
                    "Type 'Main Menu' whenever you'd like to return to the chatbot."
                ),
                state=ConversationState.LIVE_AGENT,
                quick_replies=[
                    "Main Menu"
                ]
            )

        # If we're waiting for an order number,
        # allow the user to switch topics or exit back to the main menu.
        if session["state"] == ConversationState.AWAITING_ORDER:

            message = message.strip()

            # Explicit exit phrases, so the user is never stuck needing
            # a valid order number just to leave this flow.
            if message.lower() in [
                "main menu",
                "menu",
                "back",
                "return",
                "cancel",
                "exit"
            ]:
                session["state"] = ConversationState.MAIN_MENU

                return ChatResponse(
                    reply=(
                        "No problem! 😊\n\n"
                        "You're back at the North Star Support Bot main menu."
                    ),
                    state=ConversationState.MAIN_MENU,
                    quick_replies=[
                        "Track Order",
                        "Returns",
                        "Shipping",
                        "Recommendations",
                        "Live Agent"
                    ]
                )

            intent = detect_intent(message)

            # User wants to start order tracking again
            if intent == Intent.ORDER_TRACKING:
                return ChatResponse(
                    reply="Sure! Please enter your order number (111, 222, or 333).",
                    state=ConversationState.AWAITING_ORDER,
                    quick_replies=[
                        "Main Menu"
                    ]
                )

            # User switched to another feature
            if intent != Intent.UNKNOWN:
                session["state"] = ConversationState.MAIN_MENU
                return self.process_message(session, message)

            order = ORDERS.get(message)

            if order:
                session["state"] = ConversationState.MAIN_MENU

                return ChatResponse(
                    reply=(
                        f"📦 Order #{message}\n\n"
                        f"Status: {order['status']}\n"
                        f"ETA: {order['eta']}"
                    ),
                    state=ConversationState.MAIN_MENU,
                    quick_replies=[
                        "Track Another Order",
                        "Returns",
                        "Shipping",
                        "Recommendations",
                        "Live Agent"
                    ]
                )

            return ChatResponse(
                reply=(
                    "❌ Sorry, I couldn't find that order number.\n\n"
                    "Please enter a valid order number (111, 222, or 333), "
                    "ask me about Returns, Shipping, or Recommendations, "
                    "or type 'Main Menu' to go back."
                ),
                state=ConversationState.AWAITING_ORDER,
                quick_replies=[
                    "Main Menu"
                ]
            )

        # Recommendation - Activity
        if session["state"] == ConversationState.RECOMMENDATION_ACTIVITY:

            activity = normalize_activity(message)

            if activity is None:
                return ChatResponse(
                    reply="Please choose one of the available activities.",
                    state=ConversationState.RECOMMENDATION_ACTIVITY,
                    quick_replies=[
                        "Hiking",
                        "Camping",
                        "Running"
                    ]
                )

            session["activity"] = activity
            session["state"] = ConversationState.RECOMMENDATION_WEATHER

            return ChatResponse(
                reply="Great! What weather are you expecting?",
                state=ConversationState.RECOMMENDATION_WEATHER,
                quick_replies=[
                    "Cold",
                    "Mild",
                    "Rainy"
                ]
            )


        # Recommendation - Weather
        if session["state"] == ConversationState.RECOMMENDATION_WEATHER:

            weather = normalize_weather(message)

            if weather is None:
                return ChatResponse(
                    reply="Please choose Cold, Mild, or Rainy.",
                    state=ConversationState.RECOMMENDATION_WEATHER,
                    quick_replies=[
                        "Cold",
                        "Mild",
                        "Rainy"
                    ]
                )

            session["weather"] = weather
            session["state"] = ConversationState.RECOMMENDATION_BUDGET

            return ChatResponse(
                reply="Finally, what's your budget?",
                state=ConversationState.RECOMMENDATION_BUDGET,
                quick_replies=[
                    "Under $100",
                    "$100-$250"
                ]
            )


        # Recommendation - Budget
        if session["state"] == ConversationState.RECOMMENDATION_BUDGET:

            budget = normalize_budget(message)

            if budget is None:
                return ChatResponse(
                    reply="Please choose one of the available budget ranges.",
                    state=ConversationState.RECOMMENDATION_BUDGET,
                    quick_replies=[
                        "Under $100",
                        "$100-$250"
                    ]
                )

            session["budget"] = budget

            key = (
                session["activity"],
                session["weather"],
                session["budget"],
            )

            products = RECOMMENDATIONS.get(key)

            session["state"] = ConversationState.MAIN_MENU

            if not products:
                return ChatResponse(
                    reply="Sorry, I couldn't find matching recommendations.",
                    state=ConversationState.MAIN_MENU
                )

            reply = "Here are my recommendations:\n\n"

            for product in products:
                reply += (
                    f"• {product['name']} ({product['price']})\n"
                    f"  {product['reason']}\n\n"
                )

            return ChatResponse(
                reply=reply,
                state=ConversationState.MAIN_MENU,
                quick_replies=[
                    "Track Order",
                    "Returns",
                    "Shipping",
                    "Recommendations",
                    "Live Agent"
                ]
            )
        
        # Detect the user's intent
        intent = detect_intent(message)

        if intent == Intent.GREETING:
            return ChatResponse(
                reply=(
                    "👋 Welcome to North Star Support!\n\n"
                    "How can I help you today?"
                ),
                state=ConversationState.MAIN_MENU,
                quick_replies=[
                    "Track Order",
                    "Returns",
                    "Shipping",
                    "Recommendations",
                    "Live Agent"
                ]
            )

        elif intent == Intent.ORDER_TRACKING:
            session["state"] = ConversationState.AWAITING_ORDER

            return ChatResponse(
                reply="Sure! Please enter your order number (111, 222, or 333).",
                state=ConversationState.AWAITING_ORDER
            )

        elif intent == Intent.RETURNS:
            return ChatResponse(
                reply=RETURN_POLICY,
                state=ConversationState.MAIN_MENU,
                quick_replies=[
                    "Track Order",
                    "Shipping",
                    "Recommendations",
                    "Live Agent"
                ]
            )

        elif intent == Intent.SHIPPING:
            return ChatResponse(
                reply=SHIPPING_INFO,
                state=ConversationState.MAIN_MENU,
                quick_replies=[
                    "Track Order",
                    "Returns",
                    "Recommendations",
                    "Live Agent"
                ]
            )

        elif intent == Intent.RECOMMENDATION:

            session["state"] = ConversationState.RECOMMENDATION_ACTIVITY

            return ChatResponse(
                reply=(
                    "I'd be happy to help you find the right products!\n\n"
                    "What activity are you shopping for?"
                ),
                state=ConversationState.RECOMMENDATION_ACTIVITY,
                quick_replies=[
                    "Hiking",
                    "Camping",
                    "Running"
                ]
            )

        elif intent == Intent.LIVE_AGENT:

            session["state"] = ConversationState.LIVE_AGENT

            return ChatResponse(
                reply=(
                    "👨‍💼 Connecting you with a live agent...\n\n"
                    "You are now chatting with a simulated support representative.\n\n"
                    "Type 'Main Menu' at any time to return to the chatbot."
                ),
                state=ConversationState.LIVE_AGENT,
                quick_replies=[
                    "Main Menu"
                ]
            )

        return ChatResponse(
            reply=(
                "I'm sorry, I didn't quite understand that.\n\n"
                "I can help with:\n"
                "• Order Tracking\n"
                "• Returns\n"
                "• Shipping\n"
                "• Product Recommendations\n"
                "• Live Agent"
            ),
            state=ConversationState.MAIN_MENU,
            quick_replies=[
                "Track Order",
                "Returns",
                "Shipping",
                "Recommendations",
                "Live Agent"
            ]
        )


chatbot = ChatBot()