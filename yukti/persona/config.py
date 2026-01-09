from pathlib import Path
import json

CONFIG_PATH = Path.home() / ".yukti_config.json"

DEFAULT_CONFIG = {
    "persona_plus": True
}

def load_config() -> dict:
    if not CONFIG_PATH.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    return json.loads(CONFIG_PATH.read_text())

def save_config(cfg: dict):
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))
