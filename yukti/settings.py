import json
from pathlib import Path

_SETTINGS_PATH = Path.home() / ".yukti_settings.json"

_DEFAULTS = {
    "persona_plus": False
}

def load_settings() -> dict:
    if not _SETTINGS_PATH.exists():
        return _DEFAULTS.copy()
    try:
        with open(_SETTINGS_PATH, "r") as f:
            data = json.load(f)
        return {**_DEFAULTS, **data}
    except Exception:
        return _DEFAULTS.copy()

def save_settings(settings: dict) -> None:
    with open(_SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)

def get_persona_plus() -> bool:
    return load_settings()["persona_plus"]

def set_persona_plus(enabled: bool) -> None:
    settings = load_settings()
    settings["persona_plus"] = bool(enabled)
    save_settings(settings)
