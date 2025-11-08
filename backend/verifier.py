import re
from typing import Dict, List

def verify_explanation(explanation: str, domain: str = 'agriculture') -> Dict:
    """
    Verify an AI explanation for logical consistency and completeness.
    This is a simplified version for demo purposes using pattern matching and heuristics.
    """
    
    # Parse explanation into claims
    claims = parse_claims(explanation)
    
    # Verify each claim
    verified_claims = []
    issues = []
    
    for claim in claims:
        verification = verify_claim(claim, domain)
        verified_claims.append(verification)
        
        if verification['status'] != 'valid':
            issues.append(verification)
    
    # Generate summary
    summary = generate_summary(verified_claims, issues)
    
    return {
        "original_text": explanation,
        "domain": domain,
        "claims": verified_claims,
        "issues": issues,
        "summary": summary,
        "overall_status": get_overall_status(verified_claims)
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
    
    # Check for agricultural keywords
    agri_keywords = ['water', 'irrigation', 'fertilizer', 'pesticide', 'soil', 
                     'crop', 'plant', 'harvest', 'yield', 'banana', 'potassium',
                     'spray', 'apply', 'planting', 'growing']
    
    # Check for quantitative claims
    has_numbers = bool(re.search(r'\d+', claim))
    
    # Check for causal language
    causal_words = ['because', 'therefore', 'thus', 'so', 'hence', 'due to', 
                    'result in', 'leads to', 'causes', 'based on']
    has_reasoning = any(word in claim_lower for word in causal_words)
    
    # Check for safety concerns
    safety_words = ['spray', 'apply', 'chemical', 'pesticide', 'herbicide', 'toxin']
    has_safety_concern = any(word in claim_lower for word in safety_words)
    
    # Check for missing context
    vague_words = ['optimal', 'best', 'ideal', 'maximum', 'minimum', 'good', 'better']
    is_vague = any(word in claim_lower for word in vague_words) and not has_numbers
    
    # Check for absolute claims without evidence
    absolute_words = ['always', 'never', 'all', 'every', 'none', 'guaranteed']
    is_absolute = any(word in claim_lower for word in absolute_words)
    
    # Determine status
    if is_absolute and not has_reasoning:
        status = 'invalid'
        reason = 'Makes absolute claim without justification or evidence'
        severity = 'high'
    elif is_vague:
        status = 'questionable'
        reason = 'Contains vague terms without specific measurements or context'
        severity = 'medium'
    elif has_safety_concern and not has_reasoning:
        status = 'invalid'
        reason = 'Safety-critical recommendation without justification or safety precautions'
        severity = 'high'
    elif has_numbers and not has_reasoning:
        status = 'questionable'
        reason = 'Provides specific numbers but lacks explanation or data source'
        severity = 'medium'
    elif not any(kw in claim_lower for kw in agri_keywords):
        status = 'valid'
        reason = 'General statement without specific agricultural claims'
        severity = 'low'
    else:
        status = 'valid'
        reason = 'Claim appears logically sound with appropriate context'
        severity = 'low'
    
    return {
        "claim": claim,
        "status": status,
        "reason": reason,
        "severity": severity,
        "has_data": has_numbers,
        "has_reasoning": has_reasoning,
        "requires_attention": status != 'valid'
    }

def generate_summary(verified_claims: List[Dict], issues: List[Dict]) -> Dict:
    """Generate a summary of the verification"""
    total = len(verified_claims)
    valid = sum(1 for c in verified_claims if c['status'] == 'valid')
    questionable = sum(1 for c in verified_claims if c['status'] == 'questionable')
    invalid = sum(1 for c in verified_claims if c['status'] == 'invalid')
    
    critical_issues = [i for i in issues if i['severity'] == 'high']
    
    return {
        "total_claims": total,
        "valid_claims": valid,
        "questionable_claims": questionable,
        "invalid_claims": invalid,
        "critical_issues": len(critical_issues),
        "recommendation": get_recommendation(critical_issues, invalid, questionable)
    }

def get_recommendation(critical_issues: List, invalid: int, questionable: int) -> str:
    """Generate recommendation based on verification results"""
    if len(critical_issues) > 0:
        return "⛔ STOP: Critical safety issues found. Do not proceed without expert review."
    elif invalid > 0:
        return "⚠️ CAUTION: Invalid claims detected. Verify with agricultural expert before implementing."
    elif questionable > 2:
        return "⚠️ WARNING: Multiple questionable claims. Seek additional information before proceeding."
    elif questionable > 0:
        return "✓ MOSTLY SAFE: Minor concerns detected. Review flagged items before implementing."
    else:
        return "✅ VERIFIED: All claims appear logically sound. Proceed with confidence."

def get_overall_status(claims: List[Dict]) -> str:
    """Determine overall status"""
    statuses = [c['status'] for c in claims]
    
    if 'invalid' in statuses:
        return 'invalid'
    elif 'questionable' in statuses:
        return 'questionable'
    else:
        return 'valid'
