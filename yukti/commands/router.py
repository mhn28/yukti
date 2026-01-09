"""
Central command router.
Intercepts slash-commands before LLM invocation.
"""

from yukti.commands.persona import handle_persona_command

def route_command(text: str) -> str | None:
    """
    Returns a response if command handled,
    otherwise returns None to continue to LLM.
    """
    text = text.strip()

    if text.startswith("/persona"):
        parts = text.split(maxsplit=1)
        arg = parts[1] if len(parts) > 1 else ""
        return handle_persona_command(arg)

    return None
