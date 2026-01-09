"""
Voice gating layer.
Blocks unclear ASR transcripts before LLM invocation.
"""

from yukti.voice.clarity import is_clear_statistical_query, clean_transcript


def gate_voice_input(raw_text: str) -> str | None:
    """
    Returns cleaned text if acceptable, otherwise None.
    """
    text = clean_transcript(raw_text)

    if not is_clear_statistical_query(text):
        return None

    return text
