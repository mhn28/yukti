"""
Yukti Voice Backend (Offline Only)

Policy:
- Fully local
- Open-source
- Deterministic
"""

SUPPORTED_BACKENDS = {
    "vosk": {
        "type": "offline",
        "license": "Apache-2.0",
        "description": "Kaldi/Vosk local ASR"
    }
}

DEFAULT_BACKEND = "vosk"
