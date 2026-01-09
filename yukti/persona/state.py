from yukti.config.settings import is_persona_enabled, set_persona_enabled


def persona_enabled() -> bool:
    return is_persona_enabled()


def enable_persona() -> None:
    set_persona_enabled(True)


def disable_persona() -> None:
    set_persona_enabled(False)
