DEMO_EXAMPLES = [
    {
        "id": 1,
        "title": "🍌 Banana Irrigation - Good Example",
        "domain": "agriculture",
        "explanation": "Increase watering to 50mm per week for optimal banana growth during the flowering stage. This is based on soil moisture readings showing 40% capacity and weather forecast indicating low rainfall for the next 2 weeks. Monitor for signs of overwatering such as yellowing leaves.",
        "expected_status": "valid"
    },
    {
        "id": 2,
        "title": "⚠️ Pesticide Application - Safety Issue",
        "domain": "agriculture",
        "explanation": "Spray neem oil on banana plants every day to control aphids. Use maximum concentration for best results.",
        "expected_status": "invalid"
    },
    {
        "id": 3,
        "title": "❓ Fertilizer Recommendation - Questionable",
        "domain": "agriculture",
        "explanation": "Apply 200kg per hectare of potassium sulfate for optimal banana yield. This will increase your harvest by 30%.",
        "expected_status": "questionable"
    },
    {
        "id": 4,
        "title": "✅ Harvest Timing - Well Reasoned",
        "domain": "agriculture",
        "explanation": "Harvest bananas when they reach 75% maturity (green with slight yellow tinge) because this allows for proper ripening during transport. The 3-day shipping window requires harvesting before full ripeness to prevent over-ripening. Check fruit diameter (32-38mm) and days since flowering (90-100 days) as maturity indicators.",
        "expected_status": "valid"
    },
    {
        "id": 5,
        "title": "❓ Soil Treatment - Missing Context",
        "domain": "agriculture",
        "explanation": "The soil needs lime treatment for optimal banana growth. Apply lime immediately to improve conditions.",
        "expected_status": "questionable"
    }
]
