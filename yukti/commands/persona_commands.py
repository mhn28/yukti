"""
Persona Plus command handlers.
Used by GUI, voice, and CLI.
"""

from yukti.llm.persona_state import enable_persona, disable_persona

def handle_persona_command(text: str) -> str:
    t = text.lower().strip()

    if "enable" in t and "expert" in t:
        enable_persona()
        return "Expert statistical guidance enabled."

    if "disable" in t and "expert" in t:
        disable_persona()
        return "Expert statistical guidance disabled."

    if "persona" in t and "on" in t:
        enable_persona()
        return "Persona Plus enabled."

    if "persona" in t and "off" in t:
        disable_persona()
        return "Persona Plus disabled."

    return ""
