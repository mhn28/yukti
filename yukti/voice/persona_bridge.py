from yukti.voice.pipeline import VoicePipeline
from yukti.persona.prompt import system_prompt

class VoicePersonaBridge:
    def __init__(self, vosk_model_path: str):
        self.voice = VoicePipeline(vosk_model_path)

    def capture_prompt(self) -> str:
        spoken_text = self.voice.listen_once()
        if not spoken_text:
            raise RuntimeError("No speech detected")

        persona = system_prompt()
        if persona:
            return f"{persona}\n\nUser question:\n{spoken_text}"
        return spoken_text
