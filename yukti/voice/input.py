import os
import json
import sounddevice as sd
import vosk

class VoiceInput:
    """
    Offline-only voice input using Vosk.
    """

    def __init__(self, model_path: str, samplerate: int = 16000):
        if not os.path.isdir(model_path):
            raise FileNotFoundError(f"Vosk model directory not found: {model_path}")

        self.model = vosk.Model(model_path)
        self.samplerate = samplerate

    def listen_once(self, timeout: int = 8) -> str:
        rec = vosk.KaldiRecognizer(self.model, self.samplerate)

        with sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=8000,
            dtype="int16",
            channels=1
        ) as stream:
            for _ in range(int(timeout * self.samplerate / 8000)):
                data, _ = stream.read(8000)
                if rec.AcceptWaveform(bytes(data)):
                    result = json.loads(rec.Result())
                    return result.get("text", "").strip()

        final = json.loads(rec.FinalResult())
        text = final.get("text", "").strip()
        return text if text else ""
