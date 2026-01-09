"""
ASR clarity validation for Yukti.
Rejects low-quality or non-statistical transcripts
before they reach the LLM.
"""

import re

# Minimal, conservative vocabulary
_STAT_KEYWORDS = {
    "test", "distribution", "mean", "median", "variance", "std",
    "normal", "gaussian", "shapiro", "wilcox", "bonferroni",
    "anova", "regression", "correlation", "p value", "p-value",
    "confidence", "interval", "hypothesis", "null", "alternative",
    "sample", "population"
}


def is_clear_statistical_query(text: str) -> bool:
    if not text:
        return False

    t = text.lower().strip()

    # Too short → reject
    if len(t.split()) < 4:
        return False

    # Contains at least one statistical keyword
    for kw in _STAT_KEYWORDS:
        if kw in t:
            return True

    return False


def clean_transcript(text: str) -> str:
    # Remove filler noise, normalize spaces
    text = re.sub(r"\s+", " ", text)
    return text.strip()
