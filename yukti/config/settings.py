import json
from pathlib import Path

_SETTINGS_FILE = Path.home() / ".yukti_settings.json"

_DEFAULTS = {
    "persona_plus": True
}

def load_settings() -> dict:
    if not _SETTINGS_FILE.exists():
        return _DEFAULTS.copy()
    try:
        return {**_DEFAULTS, **json.loads(_SETTINGS_FILE.read_text())}
    except Exception:
        return _DEFAULTS.copy()

def save_settings(settings: dict) -> None:
    _SETTINGS_FILE.write_text(json.dumps(settings, indent=2))

def is_persona_enabled() -> bool:
    return load_settings().get("persona_plus", True)

def set_persona_enabled(enabled: bool) -> None:
    s = load_settings()
    s["persona_plus"] = bool(enabled)
    save_settings(s)
