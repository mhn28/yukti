"""
Persona Plus Settings Interface

This module is UI-facing.
Safe to bind to:
- CLI flags
- GUI toggle
- Mobile settings switch
"""

from yukti.persona.state import (
    enable_persona,
    disable_persona,
    persona_enabled,
)

def set_persona(enabled: bool) -> None:
    if enabled:
        enable_persona()
    else:
        disable_persona()

def is_persona_enabled() -> bool:
    return persona_enabled()
