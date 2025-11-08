from flask import Flask, request, jsonify
from flask_cors import CORS
from verifier import verify_explanation
from demo_data import DEMO_EXAMPLES
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "ExplAInCheck API - Agriculture Track 🌾",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "/api/verify": "POST - Verify AI explanations",
            "/api/examples": "GET - Get demo examples"
        }
    })

@app.route('/api/verify', methods=['POST'])
def verify():
    """Main endpoint to verify AI explanations"""
    try:
        data = request.json
        explanation = data.get('explanation', '')
        domain = data.get('domain', 'agriculture')
        
        if not explanation:
            return jsonify({"error": "No explanation provided"}), 400
        
        # Run verification
        result = verify_explanation(explanation, domain)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/examples', methods=['GET'])
def get_examples():
    """Get demo examples for different scenarios"""
    return jsonify(DEMO_EXAMPLES), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
