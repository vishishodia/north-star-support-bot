ORDERS = {
    "111": {
        "status": "Shipped",
        "eta": "Arriving tomorrow"
    },
    "222": {
        "status": "Processing",
        "eta": "Ships in 24 hours"
    },
    "333": {
        "status": "Delivered",
        "eta": "Delivered"
    }
}

RETURN_POLICY = (
    "📦 Return Policy\n\n"
    "• Returns accepted within 30 days.\n"
    "• Items must be unused.\n"
    "• Original packaging is required.\n\n"
    "Start your return here:\n"
    "https://northstar.com/returns"
)

SHIPPING_INFO = (
    "🚚 Shipping Options\n\n"
    "• Standard: 3–5 business days\n"
    "• Expedited: 1–2 business days"
)

RECOMMENDATIONS = {
    ("Hiking", "Cold", "Under $100"): [
        {
            "name": "Thermal Base Layer",
            "price": "$49",
            "reason": "Keeps you warm while hiking in cold weather."
        },
        {
            "name": "Insulated Hiking Gloves",
            "price": "$35",
            "reason": "Protects your hands from low temperatures."
        },
        {
            "name": "Wool Hiking Socks",
            "price": "$20",
            "reason": "Provides warmth and moisture control."
        }
    ],

    ("Hiking", "Cold", "$100-$250"): [
        {
            "name": "Insulated Hiking Jacket",
            "price": "$180",
            "reason": "Excellent insulation for cold-weather hikes."
        },
        {
            "name": "Waterproof Hiking Boots",
            "price": "$160",
            "reason": "Keeps your feet dry and provides ankle support."
        },
        {
            "name": "Fleece Mid Layer",
            "price": "$110",
            "reason": "Adds warmth without restricting movement."
        }
    ],

    ("Camping", "Rainy", "Under $100"): [
        {
            "name": "Rain Poncho",
            "price": "$25",
            "reason": "Lightweight protection from rain."
        },
        {
            "name": "Waterproof Dry Bag",
            "price": "$30",
            "reason": "Keeps your gear dry."
        },
        {
            "name": "Camping Tarp",
            "price": "$45",
            "reason": "Provides quick rain shelter."
        }
    ],

    ("Camping", "Rainy", "$100-$250"): [
        {
            "name": "3-Person Waterproof Tent",
            "price": "$220",
            "reason": "Reliable shelter in wet conditions."
        },
        {
            "name": "Sleeping Bag",
            "price": "$120",
            "reason": "Comfortable for damp, cool nights."
        },
        {
            "name": "Camping Stove",
            "price": "$140",
            "reason": "Compact stove for outdoor cooking."
        }
    ],

    ("Running", "Mild", "Under $100"): [
        {
            "name": "Running Shoes",
            "price": "$95",
            "reason": "Comfortable daily training shoes."
        },
        {
            "name": "Moisture-Wicking T-Shirt",
            "price": "$30",
            "reason": "Helps keep you cool and dry."
        },
        {
            "name": "Sports Water Bottle",
            "price": "$15",
            "reason": "Easy hydration during runs."
        }
    ],

    ("Running", "Mild", "$100-$250"): [
        {
            "name": "Premium Running Shoes",
            "price": "$180",
            "reason": "Designed for long-distance comfort."
        },
        {
            "name": "Running Watch",
            "price": "$220",
            "reason": "Tracks pace, distance, and heart rate."
        },
        {
            "name": "Performance Running Jacket",
            "price": "$140",
            "reason": "Lightweight protection against wind."
        }
    ]
}