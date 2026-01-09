"""
LLM execution wrapper for Yukti.
All prompts pass through Persona Plus.
"""

import subprocess
from pathlib import Path
from yukti.llm.prompt_builder import build_prompt

LLAMA_BIN = Path("llama.cpp/build/bin/llama-cli")
MODEL_PATH = Path("models/llm/qwen2.5-0.5b-instruct-q4_k_m.gguf")

def run_llm(user_text: str, max_tokens: int = 256, temperature: float = 0.2) -> None:
    prompt = build_prompt(user_text)

    cmd = [
        str(LLAMA_BIN),
        "-m", str(MODEL_PATH),
        "-p", prompt,
        "-n", str(max_tokens),
        "--temp", str(temperature),
    ]

    subprocess.run(cmd, check=True)
