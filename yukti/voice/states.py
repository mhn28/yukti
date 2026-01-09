class VoiceState:
    enabled: bool = True

    @classmethod
    def enable(cls):
        cls.enabled = True

    @classmethod
    def disable(cls):
        cls.enabled = False

    @classmethod
    def is_enabled(cls) -> bool:
        return cls.enabled
