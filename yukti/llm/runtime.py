"""
Runtime configuration for local LLM execution.
"""

import os

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
