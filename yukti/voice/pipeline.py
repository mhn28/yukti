import json
import vosk
import sounddevice as sd
from pathlib import Path

SAMPLE_RATE = 16000
BLOCK_SIZE = 8000

class VoicePipeline:
    def __init__(self, model_path: str):
        model_path = Path(model_path)
        if not model_path.exists():
            raise FileNotFoundError(f"Vosk model not found: {model_path}")
        self.model = vosk.Model(str(model_path))
        self.rec = vosk.KaldiRecognizer(self.model, SAMPLE_RATE)

    def listen_once(self) -> str:
        print("\n🎙️ Listening… Speak your question clearly.\n")
        with sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=BLOCK_SIZE,
            dtype="int16",
            channels=1,
        ) as stream:
            while True:
                data, _ = stream.read(BLOCK_SIZE)
                if self.rec.AcceptWaveform(bytes(data)):
                    break
        result = json.loads(self.rec.FinalResult())
        return result.get("text", "").strip()
