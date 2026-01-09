"""
Grammar enforcement layer for offline ASR.
Uses domain constraints to reduce hallucinations
before sending text to the LLM.
"""

import re

# Allowed statistical keywords (expandable)
_ALLOWED_TERMS = [
    "test", "distribution", "normal", "shapiro", "wilcoxon",
    "anova", "regression", "correlation", "bonferroni",
    "p value", "confidence interval", "mean", "median",
    "variance", "standard deviation", "null hypothesis",
    "alternative hypothesis"
]

def enforce_statistics_grammar(text: str) -> str:
    """
    Light-weight grammar enforcement:
    - lowercases
    - removes non-statistical filler
    - keeps statistically meaningful phrases
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"[^a-z0-9\\s]", " ", text)
    text = re.sub(r"\\s+", " ", text).strip()

    kept = []
    for term in _ALLOWED_TERMS:
        if term in text:
            kept.append(term)

    # If nothing matched, fall back to original cleaned text
    return " ".join(kept) if kept else text
