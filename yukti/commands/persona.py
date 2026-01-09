"""
Persona Plus Command Handler

Usage:
  /persona on
  /persona off
  /persona status
"""

from yukti.persona.settings import (
    set_persona,
    is_persona_enabled,
)

def handle_persona_command(arg: str) -> str:
    arg = arg.strip().lower()

    if arg == "on":
        set_persona(True)
        return "Persona Plus Mode enabled."

    if arg == "off":
        set_persona(False)
        return "Persona Plus Mode disabled."

    if arg == "status":
        return (
            "Persona Plus Mode is ENABLED."
            if is_persona_enabled()
            else "Persona Plus Mode is DISABLED."
        )

    return "Usage: /persona on | off | status"
