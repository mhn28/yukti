"""
LLM Execution Engine (llama.cpp wrapper)
Handles prompt preparation and persona injection
"""

import subprocess
from pathlib import Path

from yukti.llm.persona import mount_persona
from yukti.llm.settings import get_model_path


LLAMA_BIN = Path("llama.cpp/build/bin/llama-cli")


def run_llm(prompt: str, max_tokens: int = 256, temperature: float = 0.2) -> str:
    """
    Run llama.cpp with persona-mounted prompt
    """
    model_path = get_model_path()
    final_prompt = mount_persona(prompt)

    cmd = [
        str(LLAMA_BIN),
        "-m", model_path,
        "-p", final_prompt,
        "-n", str(max_tokens),
        "--temp", str(temperature),
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout.strip()
