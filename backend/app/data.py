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
            "reason": "Keeps your feet dry while providing ankle support."
        },
        {
            "name": "Fleece Mid Layer",
            "price": "$110",
            "reason": "Adds warmth without restricting movement."
        }
    ],

    ("Hiking", "Mild", "Under $100"): [
        {
            "name": "Lightweight Hiking Shirt",
            "price": "$35",
            "reason": "Breathable fabric keeps you comfortable on the trail."
        },
        {
            "name": "Trail Cap",
            "price": "$22",
            "reason": "Protects against sun while keeping you cool."
        },
        {
            "name": "Hydration Bottle",
            "price": "$18",
            "reason": "Easy hydration during moderate hikes."
        }
    ],

    ("Hiking", "Mild", "$100-$250"): [
        {
            "name": "Premium Hiking Boots",
            "price": "$190",
            "reason": "Provides superior comfort and traction on long hikes."
        },
        {
            "name": "Lightweight Hiking Backpack",
            "price": "$140",
            "reason": "Offers ample storage with excellent weight distribution."
        },
        {
            "name": "Trekking Poles",
            "price": "$120",
            "reason": "Reduces strain on knees and improves stability on uneven terrain."
        }
    ],

    ("Hiking", "Rainy", "Under $100"): [
        {
            "name": "Waterproof Rain Jacket",
            "price": "$75",
            "reason": "Keeps you dry and comfortable during rainy hikes."
        },
        {
            "name": "Waterproof Backpack Cover",
            "price": "$20",
            "reason": "Protects your gear from getting wet."
        },
        {
            "name": "Quick-Dry Hiking Pants",
            "price": "$60",
            "reason": "Dries quickly and keeps you comfortable in wet conditions."
        }
    ],

    ("Hiking", "Rainy", "$100-$250"): [
        {
            "name": "GORE-TEX Hiking Jacket",
            "price": "$220",
            "reason": "Provides premium waterproof protection and breathability."
        },
        {
            "name": "Waterproof Hiking Boots",
            "price": "$180",
            "reason": "Keeps your feet dry while offering excellent grip on wet trails."
        },
        {
            "name": "Technical Rain Backpack",
            "price": "$140",
            "reason": "Protects your gear with built-in weather-resistant materials."
        }
    ],

    ("Camping", "Cold", "Under $100"): [
        {
            "name": "Insulated Sleeping Bag",
            "price": "$85",
            "reason": "Keeps you warm during cold camping nights."
        },
        {
            "name": "Thermal Camping Blanket",
            "price": "$35",
            "reason": "Provides extra insulation in freezing temperatures."
        },
        {
            "name": "Portable Hand Warmers",
            "price": "$20",
            "reason": "Keeps your hands warm in cold outdoor conditions."
        }
    ],

    ("Camping", "Cold", "$100-$250"): [
        {
            "name": "Four-Season Tent",
            "price": "$230",
            "reason": "Built to withstand harsh winter camping conditions."
        },
        {
            "name": "Down Sleeping Bag",
            "price": "$190",
            "reason": "Offers exceptional warmth in freezing weather."
        },
        {
            "name": "Insulated Sleeping Pad",
            "price": "$120",
            "reason": "Prevents heat loss from the cold ground."
        }
    ],

    ("Camping", "Mild", "Under $100"): [
        {
            "name": "Camping Chair",
            "price": "$45",
            "reason": "Comfortable seating for relaxing around the campsite."
        },
        {
            "name": "LED Camping Lantern",
            "price": "$30",
            "reason": "Provides bright and reliable lighting after sunset."
        },
        {
            "name": "Portable Cookware Set",
            "price": "$65",
            "reason": "Compact cooking essentials for outdoor meals."
        }
    ],

    ("Camping", "Mild", "$100-$250"): [
        {
            "name": "4-Person Camping Tent",
            "price": "$220",
            "reason": "Spacious and durable shelter for comfortable camping."
        },
        {
            "name": "Camping Cook Set",
            "price": "$130",
            "reason": "Complete cookware set for preparing meals outdoors."
        },
        {
            "name": "Portable Camping Table",
            "price": "$145",
            "reason": "Provides a stable surface for cooking and dining."
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
            "name": "Waterproof Sleeping Bag",
            "price": "$140",
            "reason": "Stays warm and dry during rainy nights."
        },
        {
            "name": "Portable Camping Stove",
            "price": "$150",
            "reason": "Reliable cooking solution for damp outdoor conditions."
        }
    ],

    ("Running", "Cold", "Under $100"): [
        {
            "name": "Thermal Running Tights",
            "price": "$55",
            "reason": "Keeps your legs warm during cold-weather runs."
        },
        {
            "name": "Running Gloves",
            "price": "$25",
            "reason": "Protects your hands from chilly temperatures."
        },
        {
            "name": "Thermal Beanie",
            "price": "$20",
            "reason": "Provides warmth while remaining lightweight."
        }
    ],

    ("Running", "Cold", "$100-$250"): [
        {
            "name": "Insulated Running Jacket",
            "price": "$170",
            "reason": "Designed to keep runners warm without overheating."
        },
        {
            "name": "Premium Winter Running Shoes",
            "price": "$190",
            "reason": "Excellent grip and insulation for cold-weather running."
        },
        {
            "name": "GPS Running Watch",
            "price": "$220",
            "reason": "Tracks your pace, distance, and heart rate year-round."
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
            "reason": "Designed for long-distance comfort and performance."
        },
        {
            "name": "GPS Running Watch",
            "price": "$220",
            "reason": "Tracks pace, heart rate, distance, and training metrics."
        },
        {
            "name": "Performance Running Jacket",
            "price": "$140",
            "reason": "Lightweight protection against wind and cool temperatures."
        }
    ],

    ("Running", "Rainy", "Under $100"): [
        {
            "name": "Water-Resistant Running Jacket",
            "price": "$75",
            "reason": "Keeps you dry during light to moderate rain."
        },
        {
            "name": "Quick-Dry Running Cap",
            "price": "$25",
            "reason": "Shields your face from rain while staying breathable."
        },
        {
            "name": "Anti-Slip Running Socks",
            "price": "$20",
            "reason": "Improves comfort and grip in wet conditions."
        }
    ],

    ("Running", "Rainy", "$100-$250"): [
        {
            "name": "Waterproof Running Shoes",
            "price": "$170",
            "reason": "Keeps your feet dry while maintaining excellent traction."
        },
        {
            "name": "Premium Waterproof Running Jacket",
            "price": "$200",
            "reason": "Provides superior rain protection with breathable fabric."
        },
        {
            "name": "GPS Sports Watch",
            "price": "$230",
            "reason": "Tracks performance accurately in all weather conditions."
        }
    ]
}