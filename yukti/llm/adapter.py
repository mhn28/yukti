from yukti.persona.prompt import system_prompt
from yukti.config.settings import is_persona_enabled

def prepare_prompt(user_input: str) -> str:
    """
    Assemble the final prompt sent to the LLM.
    Persona Plus is injected automatically if enabled.
    """
    persona = system_prompt() if is_persona_enabled() else ""
    if persona:
        return f"{persona}\n\nUser: {user_input}\nAssistant:"
    return f"User: {user_input}\nAssistant:"
