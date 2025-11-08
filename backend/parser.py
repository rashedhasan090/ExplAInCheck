"""Parser module for extracting logical statements from AI explanations."""

import re
from typing import List, Dict, Any
import spacy

# Load spaCy model for NLP processing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


class ExplanationParser:
    """Parse AI-generated explanations into logical statements."""
    
    def __init__(self):
        self.causal_patterns = [
            r"because",
            r"since",
            r"therefore",
            r"thus",
            r"hence",
            r"as a result",
            r"consequently",
            r"due to",
            r"leads to",
            r"causes"
        ]
        
    def parse_explanation(self, explanation: str) -> Dict[str, Any]:
        """Parse an explanation into structured logical components.
        
        Args:
            explanation: The AI-generated explanation text
            
        Returns:
            Dictionary containing parsed components:
            - sentences: List of individual sentences
            - logical_steps: List of logical reasoning steps
            - assumptions: List of implicit/explicit assumptions
            - causal_chains: List of cause-effect relationships
        """
        doc = nlp(explanation)
        
        result = {
            "sentences": self._extract_sentences(doc),
            "logical_steps": self._extract_logical_steps(doc),
            "assumptions": self._extract_assumptions(doc),
            "causal_chains": self._extract_causal_chains(doc),
            "entities": self._extract_entities(doc)
        }
        
        return result
    
    def _extract_sentences(self, doc) -> List[str]:
        """Extract individual sentences from the text."""
        return [sent.text.strip() for sent in doc.sents]
    
    def _extract_logical_steps(self, doc) -> List[Dict[str, str]]:
        """Extract logical reasoning steps from the explanation."""
        steps = []
        step_markers = ["first", "second", "third", "finally", "then", "next"]
        
        for i, sent in enumerate(doc.sents):
            sent_text = sent.text.lower()
            for marker in step_markers:
                if marker in sent_text:
                    steps.append({
                        "step": i + 1,
                        "marker": marker,
                        "content": sent.text.strip()
                    })
                    break
        
        return steps
    
    def _extract_assumptions(self, doc) -> List[str]:
        """Extract assumptions from the explanation."""
        assumptions = []
        assumption_patterns = [
            r"assuming",
            r"if we assume",
            r"given that",
            r"provided that",
            r"suppose",
            r"let's say"
        ]
        
        for sent in doc.sents:
            sent_text = sent.text.lower()
            for pattern in assumption_patterns:
                if re.search(pattern, sent_text):
                    assumptions.append(sent.text.strip())
                    break
        
        return assumptions
    
    def _extract_causal_chains(self, doc) -> List[Dict[str, str]]:
        """Extract cause-effect relationships."""
        causal_chains = []
        
        for sent in doc.sents:
            sent_text = sent.text.lower()
            for pattern in self.causal_patterns:
                if re.search(pattern, sent_text):
                    # Split sentence on causal word
                    parts = re.split(pattern, sent_text, maxsplit=1)
                    if len(parts) == 2:
                        causal_chains.append({
                            "cause": parts[0].strip(),
                            "effect": parts[1].strip(),
                            "connector": pattern
                        })
                    break
        
        return causal_chains
    
    def _extract_entities(self, doc) -> List[Dict[str, str]]:
        """Extract named entities and key terms."""
        entities = []
        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_
            })
        return entities
    
    def to_logical_form(self, parsed_data: Dict[str, Any]) -> List[str]:
        """Convert parsed data into logical statements.
        
        Args:
            parsed_data: Output from parse_explanation()
            
        Returns:
            List of logical statements in simplified form
        """
        logical_statements = []
        
        # Convert causal chains to implications
        for chain in parsed_data.get("causal_chains", []):
            statement = f"IF ({chain['cause']}) THEN ({chain['effect']})"
            logical_statements.append(statement)
        
        # Convert assumptions to predicates
        for assumption in parsed_data.get("assumptions", []):
            statement = f"ASSUME: {assumption}"
            logical_statements.append(statement)
        
        return logical_statements
