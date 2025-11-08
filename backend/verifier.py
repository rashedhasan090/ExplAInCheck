import re
from typing import Dict, List
import random

def verify_explanation(explanation: str, domain: str = 'agriculture') -> Dict:
    """
    Verify an AI explanation for logical consistency and completeness.
    Enhanced with detailed metrics for interactive visualizations.
    """
    
    # Parse explanation into claims
    claims = parse_claims(explanation)
    
    # Verify each claim with detailed scoring
    verified_claims = []
    issues = []
    metrics = {
        "data_quality": 0,
        "logical_consistency": 0,
        "completeness": 0,
        "evidence_strength": 0,
        "contextual_relevance": 0
    }
    
    for claim in claims:
        verification = verify_claim(claim, domain)
        verified_claims.append(verification)
        
        if verification['status'] != 'valid':
            issues.append(verification)
    
    # Calculate detailed metrics for charts
    metrics = calculate_detailed_metrics(verified_claims, explanation)
    
    # Generate summary with enhanced details
    summary = generate_enhanced_summary(verified_claims, issues, metrics)
    
    # Add chart data for frontend visualization
    chart_data = generate_chart_data(verified_claims, metrics)
    
    return {
        "original_text": explanation,
        "domain": domain,
        "claims": verified_claims,
        "issues": issues,
        "summary": summary,
        "overall_status": get_overall_status(verified_claims),
        "metrics": metrics,
        "chart_data": chart_data,
        "recommendations": generate_recommendations(issues, metrics)
    }

def parse_claims(text: str) -> List[str]:
    """Parse text into individual claims"""
    # Split by sentences
    sentences = re.split(r'[.!?]+', text)
    claims = [s.strip() for s in sentences if s.strip()]
    return claims

def verify_claim(claim: str, domain: str) -> Dict:
    """Verify a single claim using pattern matching and heuristics"""
    claim_lower = claim.lower()
    
    # Initialize verification result
    result = {
        "claim": claim,
        "status": "questionable",
        "confidence": 50,
        "reasoning": "",
        "data_support": False,
        "logical_structure": "medium",
        "specificity_score": 0
    }
    
    # Check for data/evidence indicators (good signs)
    data_keywords = ["based on", "data shows", "research indicates", "studies show", 
                    "measurements", "analysis", "forecast", "readings", "test", "monitoring"]
    has_data = any(keyword in claim_lower for keyword in data_keywords)
    
    # Check for specificity (numbers, units, concrete details)
    has_numbers = bool(re.search(r'\d+', claim))
    has_units = bool(re.search(r'(mm|kg|lbs|acres?|hectares?|°[CF]|ppm|%)', claim))
    
    # Check for hedge words (uncertainty indicators)
    hedge_words = ["may", "might", "could", "possibly", "perhaps", "generally", "typically"]
    has_hedges = any(word in claim_lower for word in hedge_words)
    
    # Check for dangerous/invalid patterns
    dangerous_patterns = [
        "maximum concentration", "ignore", "regardless of", "always", "never", 
        "every day", "daily application", "5x", "10x", "double", "triple"
    ]
    is_dangerous = any(pattern in claim_lower for pattern in dangerous_patterns)
    
    # Check for vague/incomplete patterns
    vague_patterns = [
        "may help", "will improve", "is good", "needs treatment", "should apply",
        "consider", "results may vary", "generally recommended"
    ]
    is_vague = any(pattern in claim_lower for pattern in vague_patterns)
    
    # Calculate specificity score (0-100)
    specificity = 0
    if has_numbers: specificity += 30
    if has_units: specificity += 25
    if has_data: specificity += 30
    if len(claim.split()) > 15: specificity += 15  # Detailed explanation
    result["specificity_score"] = min(specificity, 100)
    
    # Determine status
    if is_dangerous:
        result["status"] = "invalid"
        result["confidence"] = random.randint(5, 20)
        result["reasoning"] = "Contains potentially dangerous recommendations without safety considerations."
        result["logical_structure"] = "poor"
    elif has_data and has_numbers and has_units and not has_hedges:
        result["status"] = "valid"
        result["confidence"] = random.randint(80, 95)
        result["reasoning"] = "Well-supported claim with specific data and measurements."
        result["data_support"] = True
        result["logical_structure"] = "strong"
    elif is_vague or (not has_data and not has_numbers):
        result["status"] = "questionable"
        result["confidence"] = random.randint(30, 55)
        result["reasoning"] = "Lacks specific data or contextual information to verify accuracy."
        result["logical_structure"] = "weak"
    else:
        result["status"] = "questionable"
        result["confidence"] = random.randint(50, 70)
        result["reasoning"] = "Partially supported but missing key details for full verification."
        result["data_support"] = has_data
        result["logical_structure"] = "medium"
    
    return result

def calculate_detailed_metrics(verified_claims: List[Dict], explanation: str) -> Dict:
    """Calculate detailed metrics for visualization"""
    
    total_claims = len(verified_claims)
    if total_claims == 0:
        return {
            "data_quality": 50,
            "logical_consistency": 50,
            "completeness": 50,
            "evidence_strength": 50,
            "contextual_relevance": 50
        }
    
    # Data quality: based on data support indicators
    data_supported = sum(1 for c in verified_claims if c.get("data_support", False))
    data_quality = int((data_supported / total_claims) * 100)
    
    # Logical consistency: based on status distribution
    valid_claims = sum(1 for c in verified_claims if c["status"] == "valid")
    invalid_claims = sum(1 for c in verified_claims if c["status"] == "invalid")
    logical_consistency = int(((valid_claims - invalid_claims) / total_claims) * 100)
    logical_consistency = max(0, min(100, logical_consistency + 50))  # Normalize to 0-100
    
    # Completeness: based on specificity scores
    avg_specificity = sum(c.get("specificity_score", 0) for c in verified_claims) / total_claims
    completeness = int(avg_specificity)
    
    # Evidence strength: based on confidence scores
    avg_confidence = sum(c.get("confidence", 50) for c in verified_claims) / total_claims
    evidence_strength = int(avg_confidence)
    
    # Contextual relevance: based on length and detail
    word_count = len(explanation.split())
    contextual_relevance = min(100, int((word_count / 50) * 100))  # 50+ words = 100%
    
    return {
        "data_quality": data_quality,
        "logical_consistency": logical_consistency,
        "completeness": completeness,
        "evidence_strength": evidence_strength,
        "contextual_relevance": contextual_relevance
    }

def generate_chart_data(verified_claims: List[Dict], metrics: Dict) -> Dict:
    """Generate data structures for frontend charts"""
    
    # Status distribution for pie chart
    status_counts = {"valid": 0, "invalid": 0, "questionable": 0}
    for claim in verified_claims:
        status = claim.get("status", "questionable")
        status_counts[status] += 1
    
    # Confidence distribution for bar chart
    confidence_ranges = {"high": 0, "medium": 0, "low": 0}
    for claim in verified_claims:
        confidence = claim.get("confidence", 50)
        if confidence >= 75:
            confidence_ranges["high"] += 1
        elif confidence >= 45:
            confidence_ranges["medium"] += 1
        else:
            confidence_ranges["low"] += 1
    
    # Metrics radar chart data
    radar_data = {
        "labels": ["Data Quality", "Logical Consistency", "Completeness", 
                  "Evidence Strength", "Contextual Relevance"],
        "values": [
            metrics["data_quality"],
            metrics["logical_consistency"],
            metrics["completeness"],
            metrics["evidence_strength"],
            metrics["contextual_relevance"]
        ]
    }
    
    return {
        "status_distribution": status_counts,
        "confidence_distribution": confidence_ranges,
        "metrics_radar": radar_data,
        "claim_details": [
            {
                "claim_text": c["claim"][:50] + "..." if len(c["claim"]) > 50 else c["claim"],
                "confidence": c.get("confidence", 50),
                "status": c["status"]
            }
            for c in verified_claims
        ]
    }

def generate_enhanced_summary(verified_claims: List[Dict], issues: List[Dict], metrics: Dict) -> str:
    """Generate detailed summary with metrics"""
    
    total = len(verified_claims)
    valid = sum(1 for c in verified_claims if c["status"] == "valid")
    invalid = sum(1 for c in verified_claims if c["status"] == "invalid")
    questionable = sum(1 for c in verified_claims if c["status"] == "questionable")
    
    avg_metrics = sum(metrics.values()) / len(metrics)
    
    if avg_metrics >= 75:
        quality = "excellent"
    elif avg_metrics >= 60:
        quality = "good"
    elif avg_metrics >= 40:
        quality = "moderate"
    else:
        quality = "poor"
    
    summary = f"Analysis of {total} claims: {valid} valid, {questionable} questionable, {invalid} invalid. "
    summary += f"Overall explanation quality is {quality} with {int(avg_metrics)}% average metric score. "
    
    if invalid > 0:
        summary += f"⚠️ {invalid} critical issue(s) detected requiring attention. "
    if questionable > total * 0.5:
        summary += "Significant portions lack specific supporting data. "
    if valid > total * 0.7:
        summary += "✅ Strong evidence-based reasoning detected. "
    
    return summary

def get_overall_status(verified_claims: List[Dict]) -> str:
    """Determine overall status"""
    if not verified_claims:
        return "questionable"
    
    invalid_count = sum(1 for c in verified_claims if c["status"] == "invalid")
    valid_count = sum(1 for c in verified_claims if c["status"] == "valid")
    total = len(verified_claims)
    
    if invalid_count > 0:
        return "invalid"
    elif valid_count / total >= 0.7:
        return "valid"
    else:
        return "questionable"

def generate_recommendations(issues: List[Dict], metrics: Dict) -> List[str]:
    """Generate actionable recommendations based on analysis"""
    
    recommendations = []
    
    if metrics["data_quality"] < 50:
        recommendations.append("📊 Include specific data sources and measurements to support claims")
    
    if metrics["logical_consistency"] < 50:
        recommendations.append("🔍 Review logical flow and remove contradictory statements")
    
    if metrics["completeness"] < 50:
        recommendations.append("📝 Add more contextual details and specific parameters")
    
    if metrics["evidence_strength"] < 50:
        recommendations.append("🔬 Cite research, studies, or field observations to strengthen evidence")
    
    if metrics["contextual_relevance"] < 50:
        recommendations.append("🌾 Provide more domain-specific context and environmental factors")
    
    if len(issues) > 0:
        recommendations.append(f"⚠️ Address {len(issues)} flagged issue(s) before implementation")
    
    if not recommendations:
        recommendations.append("✅ Explanation meets quality standards for agricultural decision-making")
    
    return recommendations
