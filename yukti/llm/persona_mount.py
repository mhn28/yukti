"""
Persona Mount Assembly
Injects Persona Plus into every LLM prompt
"""

from yukti.persona.default import DEFAULT_PERSONA


def apply_persona(user_prompt: str) -> str:
    persona_header = f"""
You are {DEFAULT_PERSONA['name']}.

Role:
{DEFAULT_PERSONA['role']}

Expertise:
- """ + "\n- ".join(DEFAULT_PERSONA["scope"]) + """

Style:
Tone: {DEFAULT_PERSONA['style']['tone']}
Verbosity: {DEFAULT_PERSONA['style']['verbosity']}
Assumptions: {DEFAULT_PERSONA['style']['assumptions']}
Math usage: {DEFAULT_PERSONA['style']['math']}

Rules:
- """ + "\n- ".join(DEFAULT_PERSONA["rules"]) + """

User question:
"""
    return persona_header + user_prompt.strip()
