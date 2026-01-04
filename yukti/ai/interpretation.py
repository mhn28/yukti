"""
Phase 34: Controlled Local LLM Interpretation Engine

Rules:
- LLM is NEVER authoritative
- Must be explicitly enabled by user
- Input is structured analysis output, not raw data
- Output is clearly labeled as interpretive
"""

from datetime import datetime

DISCLAIMER = (
    "⚠️ AI-Generated Interpretation (Non-Authoritative): "
    "This text is intended for exploratory reasoning only. "
    "All scientific conclusions must be verified manually."
)

class LLMInterpretationError(RuntimeError):
    pass

def interpret_results(
    analysis_summary: dict,
    enabled: bool = False,
    model_name: str | None = None
):
    if not enabled:
        raise LLMInterpretationError(
            "LLM interpretation requested without explicit opt-in."
        )

    if not model_name:
        raise LLMInterpretationError(
            "No local LLM model specified."
        )

    # NOTE: actual model invocation is deliberately abstracted
    # Yukti never bundles or auto-downloads models

    prompt = (
        "You are assisting with scientific interpretation.\n"
        "Do NOT assert causality.\n"
        "Do NOT fabricate citations.\n"
        "Explain results conservatively.\n\n"
        f"ANALYSIS SUMMARY:\n{analysis_summary}\n"
    )

    return {
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "model": model_name,
        "disclaimer": DISCLAIMER,
        "prompt_used": prompt,
        "interpretation": "<LOCAL LLM OUTPUT HERE>"
    }
