"""
Runtime configuration for local LLM execution.
Public, stable API for voice / CLI / GUI.
"""

import os
from yukti.llm.runner import run_llm as _run_llm

LLAMA_CLI = os.environ.get(
    "YUKTI_LLAMA_CLI",
    "/Volumes/mhn_AI/dev/yukti/llama.cpp/build/bin/llama-cli"
)

def llama_cli_path() -> str:
    if not os.path.isfile(LLAMA_CLI):
        raise FileNotFoundError(
            f"llama-cli not found at: {LLAMA_CLI}\n"
            "Set YUKTI_LLAMA_CLI environment variable if needed."
        )
    return LLAMA_CLI


def invoke_llm(prompt: str) -> None:
    """
    Public, stable entrypoint for all non-GUI callers
    (voice, CLI, tests).
    """
    if not prompt or not prompt.strip():
        print("❌ Empty prompt, aborting LLM call.")
        return

    _run_llm(prompt)
