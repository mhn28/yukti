from yukti.voice.listener import listen_with_grammar
from yukti.runtime.confirm import confirm_text
from yukti.persona.state import persona_enabled
from yukti.llm.adapter import prepare_prompt
import subprocess, shlex, os

ASR_MODEL = "models/vosk-model-en-us-0.22"
GRAMMAR = "yukti/voice/grammar/statistics.jsgf"
LLM_MODEL = "models/llm/qwen2.5-0.5b-instruct-q4_k_m.gguf"
LLAMA = "/Volumes/mhn_AI/dev/yukti/llama.cpp/build/bin/llama-cli"

print("\n🧠 Persona Plus:", persona_enabled())

spoken = listen_with_grammar(ASR_MODEL, GRAMMAR)
final_text = confirm_text(spoken)

if not final_text:
    print("\n❌ Cancelled.")
    exit(0)

prompt = prepare_prompt(final_text)

cmd = f"{LLAMA} -m {shlex.quote(LLM_MODEL)} -p {shlex.quote(prompt)} -n 256 --temp 0.2"
subprocess.run(cmd, shell=True)
