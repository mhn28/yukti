"""
Global runtime switch for Persona Plus.
"""

_PERSONA_ENABLED = True  # default ON

def enable_persona():
    global _PERSONA_ENABLED
    _PERSONA_ENABLED = True

def disable_persona():
    global _PERSONA_ENABLED
    _PERSONA_ENABLED = False

def persona_enabled() -> bool:
    return _PERSONA_ENABLED
