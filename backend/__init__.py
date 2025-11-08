"""ExplAInCheck Backend - AI Explanation Verification System"""

from .parser import ExplanationParser
from .verifier import LogicalVerifier

__version__ = "0.1.0"
__all__ = ["ExplanationParser", "LogicalVerifier"]
