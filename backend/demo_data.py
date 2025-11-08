# 500 Comprehensive Agriculture Demo Scenarios for ExplAInCheck
# Auto-generated scenarios covering diverse agricultural domains

import random

# Base categories and parameters for scenario generation
CROP_TYPES = ["banana", "corn", "wheat", "rice", "soybean", "tomato", "potato", "cotton", "sugarcane", "coffee"]
ISSUES = ["irrigation", "pest_control", "fertilization", "harvest", "soil", "disease", "weather", "equipment"]
SEVERITIES = ["minor", "moderate", "severe", "critical"]

def generate_demo_scenarios():
    """Generate 500 diverse agriculture scenarios"""
    scenarios = []
    
    # Manually crafted high-quality scenarios (first 100)
    base_scenarios = [
        {
            "id": 1,
            "title": "🍌 Banana Irrigation - Optimal Scheduling",
            "domain": "agriculture",
            "category": "irrigation",
            "explanation": "Increase watering to 50mm per week for optimal banana growth during flowering stage. Based on soil moisture at 40% capacity, ET rate of 35mm/week, temperature 28°C, and 70% humidity. Root zone depth is 60cm with sandy loam texture requiring frequent irrigation.",
            "expected_status": "valid",
            "confidence_score": 92,
            "reasoning_quality": "high",
            "data_sources": ["soil_moisture_sensor", "weather_station", "ET_model"]
        },
        {
            "id": 2,
            "title": "⚠️ Pesticide Overuse - Safety Issue",
            "domain": "agriculture",
            "category": "pest_control",
            "explanation": "Spray neem oil daily at maximum concentration during midday sun for aphid control. Apply regardless of pest population levels.",
            "expected_status": "invalid",
            "confidence_score": 15,
            "reasoning_quality": "low",
            "data_sources": []
        },
        {
            "id": 3,
            "title": "❓ Fertilizer - Incomplete Data",
            "domain": "agriculture",
            "category": "fertilization",
            "explanation": "Apply 200kg/hectare potassium sulfate for banana yield increase of 30%. Based on general tropical crop recommendations.",
            "expected_status": "questionable",
            "confidence_score": 45,
            "reasoning_quality": "medium",
            "data_sources": ["general_guidelines"]
        },
        {
            "id": 4,
            "title": "✅ Harvest Timing - Data-Driven",
            "domain": "agriculture",
            "category": "harvest",
            "explanation": "Harvest bananas at 75% maturity (green with yellow tinge) for 3-day shipping window. Firmness 8-9 on penetrometer prevents bruising. Temperature during transport will be 15-18°C which maintains fruit quality. Historical data shows 5% less spoilage vs earlier harvest.",
            "expected_status": "valid",
            "confidence_score": 88,
            "reasoning_quality": "high",
            "data_sources": ["penetrometer_readings", "shipping_data", "quality_analytics"]
        },
        {
            "id": 5,
            "title": "❓ Soil pH - Missing Context",
            "domain": "agriculture",
            "category": "soil",
            "explanation": "Apply lime treatment immediately for banana growth. This will improve soil conditions and plant health.",
            "expected_status": "questionable",
            "confidence_score": 38,
            "reasoning_quality": "low",
            "data_sources": []
        },
        {
            "id": 6,
            "title": "🌽 Corn Planting Density - Precision Agriculture",
            "domain": "agriculture",
            "category": "planting",
            "explanation": "Plant 32,000 seeds/acre with 30-inch rows. Soil test shows N=45ppm, P=28ppm. Historical yield is 185 bu/acre at this density. Forecast: 24 inches rainfall during season supports population without water stress. Field capacity is 2.8 inches/foot in top 4 feet.",
            "expected_status": "valid",
            "confidence_score": 91,
            "reasoning_quality": "high",
            "data_sources": ["soil_test_lab", "yield_history", "weather_forecast", "soil_survey"]
        },
        {
            "id": 7,
            "title": "⚠️ Herbicide Misapplication - Dangerous",
            "domain": "agriculture",
            "category": "pest_control",
            "explanation": "Apply glyphosate at 5x recommended concentration in windy conditions for faster weed kill. Rain not needed, spray anytime.",
            "expected_status": "invalid",
            "confidence_score": 8,
            "reasoning_quality": "very_low",
            "data_sources": []
        },
        {
            "id": 8,
            "title": "🍅 Early Blight Management - Comprehensive",
            "domain": "agriculture",
            "category": "disease",
            "explanation": "Apply copper fungicide (2.5 lbs/acre) for early blight on tomatoes. Visual inspection shows concentric rings on lower leaves. Temperature 60-80°F optimal for application. 7-day humidity average 78% indicates moderate disease pressure. Disease model predicts severe infection risk in 72 hours. Resistant varieties unavailable for heirloom types.",
            "expected_status": "valid",
            "confidence_score": 89,
            "reasoning_quality": "high",
            "data_sources": ["field_scouting", "weather_station", "disease_model", "variety_database"]
        },
        {
            "id": 9,
            "title": "🌾 Wheat Nitrogen Timing - Split Application",
            "domain": "agriculture",
            "category": "fertilization",
            "explanation": "Apply nitrogen in split: 80 lbs/acre at planting, 60 lbs at tillering (Feekes 4-5 stage). Soil test shows residual N at 25 ppm. Target yield 70 bu/acre requires 2.5 lbs N/bushel. Spring rainfall forecast is above average (15 inches) increasing leaching risk, justifying split application to improve N use efficiency from 50% to 70%.",
            "expected_status": "valid",
            "confidence_score": 87,
            "reasoning_quality": "high",
            "data_sources": ["soil_test", "yield_goal", "rainfall_forecast", "N_calculator"]
        },
        {
            "id": 10,
            "title": "⚠️ Tillage Recommendation - Erosion Risk",
            "domain": "agriculture",
            "category": "soil",
            "explanation": "Use deep moldboard plow on 15% slope field after harvest. Till when soil is wet for easier operation. Leave field bare over winter.",
            "expected_status": "invalid",
            "confidence_score": 12,
            "reasoning_quality": "very_low",
            "data_sources": []
        },
    ]
    
    scenarios.extend(base_scenarios)
    
    # Generate remaining 490 scenarios programmatically with variations
    for i in range(11, 501):
        scenario_type = random.choice(["valid", "invalid", "questionable"])
        crop = random.choice(CROP_TYPES)
        issue_type = random.choice(ISSUES)
        
        if scenario_type == "valid":
            scenarios.append({
                "id": i,
                "title": f"✅ {crop.title()} {issue_type.replace('_', ' ').title()} - Scenario {i}",
                "domain": "agriculture",
                "category": issue_type,
                "explanation": f"Evidence-based recommendation for {crop} {issue_type.replace('_', ' ')} management. Analysis includes soil conditions (pH 6.5, moisture 65%), weather forecast (temp 22-28°C, rainfall 40mm expected), historical yield data showing 15% improvement with this approach, and pest pressure monitoring indicating {random.choice(['low', 'moderate'])} risk. Root zone analysis supports this timing.",
                "expected_status": "valid",
                "confidence_score": random.randint(80, 95),
                "reasoning_quality": "high",
                "data_sources": ["sensor_network", "satellite_imagery", "historical_records", "lab_analysis"]
            })
        elif scenario_type == "invalid":
            scenarios.append({
                "id": i,
                "title": f"⚠️ {crop.title()} {issue_type.replace('_', ' ').title()} - Risk {i}",
                "domain": "agriculture",
                "category": issue_type,
                "explanation": f"Apply excessive treatment for {crop} without testing. Use maximum rates regardless of conditions. Ignore safety guidelines and environmental factors. Treat all areas uniformly without assessment.",
                "expected_status": "invalid",
                "confidence_score": random.randint(5, 20),
                "reasoning_quality": "very_low",
                "data_sources": []
            })
        else:  # questionable
            scenarios.append({
                "id": i,
                "title": f"❓ {crop.title()} {issue_type.replace('_', ' ').title()} - Unclear {i}",
                "domain": "agriculture",
                "category": issue_type,
                "explanation": f"General recommendation for {crop} {issue_type.replace('_', ' ')}. Standard approach may help. Consider applying treatment. Results may vary.",
                "expected_status": "questionable",
                "confidence_score": random.randint(35, 55),
                "reasoning_quality": "medium",
                "data_sources": ["general_guidelines"]
            })
    
    return scenarios

# Generate all scenarios
DEMO_EXAMPLES = generate_demo_scenarios()

def get_random_demo():
    """Return a random demo for frontend"""
    return random.choice(DEMO_EXAMPLES)

def search_similar_demos(user_input, threshold=0.6):
    """Find similar demos based on user input using fuzzy matching"""
    import difflib
    
    user_lower = user_input.lower()
    matches = []
    
    for demo in DEMO_EXAMPLES:
        explanation_lower = demo["explanation"].lower()
        title_lower = demo["title"].lower()
        
        # Calculate similarity scores
        explanation_ratio = difflib.SequenceMatcher(None, user_lower, explanation_lower).ratio()
        title_ratio = difflib.SequenceMatcher(None, user_lower, title_lower).ratio()
        
        # Check for keyword matches
        keywords = ["irrigation", "water", "pest", "fertilizer", "harvest", "soil", "disease", 
                   "spray", "plant", "crop", "yield"]
        keyword_matches = sum(1 for kw in keywords if kw in user_lower and kw in explanation_lower)
        keyword_score = keyword_matches / len(keywords)
        
        # Combined score
        overall_score = max(explanation_ratio, title_ratio) + (keyword_score * 0.3)
        
        if overall_score >= threshold:
            matches.append({
                "demo": demo,
                "similarity": overall_score,
                "match_type": "similar_scenario"
            })
    
    # Sort by similarity
    matches.sort(key=lambda x: x["similarity"], reverse=True)
    return matches[:5] if matches else None  # Return top 5 matches
