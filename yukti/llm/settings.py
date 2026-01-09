"""
LLM runtime settings
User-toggleable, persistent-safe
"""

from pathlib import Path

# ===== MODEL PATH =====
MODEL_PATH = Path("models/llm/qwen2.5-0.5b-instruct-q4_k_m.gguf")

# ===== PERSONA SETTINGS =====
PERSONA_PLUS_ENABLED = True   # DEFAULT ON


def get_model_path() -> str:
    return str(MODEL_PATH.resolve())


def persona_enabled() -> bool:
    """
    Central toggle for Persona Plus Mode
    """
    return PERSONA_PLUS_ENABLED
