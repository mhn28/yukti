"""
Prompt construction for Yukti LLM.
Handles Persona Plus injection.
"""

from yukti.persona.system_prompt import system_prompt

def build_prompt(user_text: str) -> str:
    """
    Build the final prompt sent to the LLM.
    """
    persona = system_prompt()
    if persona:
        return f"{persona}\n\nUser:\n{user_text}\n\nAssistant:"
    return f"User:\n{user_text}\n\nAssistant:"
