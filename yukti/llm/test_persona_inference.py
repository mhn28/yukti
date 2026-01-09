from yukti.persona.state import enable_persona, disable_persona
from yukti.llm.adapter import prepare_prompt

QUESTION = "What is the Bonferroni correction?"

print("\n--- Persona OFF ---\n")
disable_persona()
print(prepare_prompt(QUESTION))

print("\n--- Persona ON ---\n")
enable_persona()
print(prepare_prompt(QUESTION))
