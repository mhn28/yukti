"""
Voice feedback when ASR input is unclear.
"""

def repeat_request_message() -> str:
    return (
        "I didn’t clearly understand your question. "
        "Please repeat it slowly and clearly, focusing on one statistical concept."
    )
