from flask import Flask, request, jsonify
from flask_cors import CORS
from verifier import verify_explanation
from demo_data import DEMO_EXAMPLES, get_random_demo, search_similar_demos
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "ExplAInCheck API - Agriculture Track 🌽",
        "status": "running",
        "version": "2.0.0",
        "endpoints": {
            "/api/verify": "POST - Verify AI explanations with detailed analysis",
            "/api/examples": "GET - Get all demo examples",
            "/api/random-demo": "GET - Get random demo scenario",
            "/api/search-similar": "POST - Find similar scenarios (fuzzy matching)"
        }
    })

@app.route('/api/verify', methods=['POST'])
def verify():
    """Main endpoint to verify AI explanations with enhanced analysis"""
    try:
        data = request.json
        explanation = data.get('explanation', '')
        domain = data.get('domain', 'agriculture')
        
        if not explanation:
            return jsonify({"error": "No explanation provided"}), 400
        
        # Check for similar demos first (fuzzy matching)
        similar_matches = search_similar_demos(explanation, threshold=0.5)
        
        if similar_matches and len(similar_matches) > 0:
            # Use the best matching demo
            best_match = similar_matches[0]
            demo = best_match["demo"]
            
            # Run verification with enhanced context
            result = verify_explanation(explanation, domain)
            
            # Add similarity information and recommendations
            result["similarity_match"] = {
                "found": True,
                "similarity_score": round(best_match["similarity"] * 100, 1),
                "matched_scenario": demo["title"],
                "category": demo.get("category", "general"),
                "recommendation": f"Your input is {round(best_match['similarity'] * 100, 1)}% similar to a known scenario. Consider the following approach..."
            }
            
            # Add scenario-specific metrics
            result["enhanced_metrics"] = {
                "confidence_score": demo.get("confidence_score", 50),
                "reasoning_quality": demo.get("reasoning_quality", "medium"),
                "data_sources_count": len(demo.get("data_sources", [])),
                "expected_outcome": demo.get("expected_status", "questionable")
            }
            
            return jsonify(result), 200
        else:
            # Run standard verification for novel input
            result = verify_explanation(explanation, domain)
            
            result["similarity_match"] = {
                "found": False,
                "message": "This appears to be a novel scenario. Analysis is based on general principles."
            }
            
            return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/examples', methods=['GET'])
def get_examples():
    """Get all demo examples for different scenarios"""
    return jsonify(DEMO_EXAMPLES), 200

@app.route('/api/random-demo', methods=['GET'])
def get_random_example():
    """Get a random demo scenario for testing"""
    try:
        demo = get_random_demo()
        return jsonify({
            "success": True,
            "demo": demo
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/search-similar', methods=['POST'])
def search_similar():
    """Search for similar demo scenarios based on user input"""
    try:
        data = request.json
        user_input = data.get('input', '')
        threshold = data.get('threshold', 0.6)
        
        if not user_input:
            return jsonify({"error": "No input provided"}), 400
        
        matches = search_similar_demos(user_input, threshold)
        
        if matches:
            return jsonify({
                "success": True,
                "matches_found": len(matches),
                "matches": matches
            }), 200
        else:
            return jsonify({
                "success": True,
                "matches_found": 0,
                "message": "No similar scenarios found. This appears to be a novel case."
            }), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
