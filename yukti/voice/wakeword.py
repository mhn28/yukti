import json
import sounddevice as sd
import vosk

class WakeWordDetector:
    """
    Offline wake-word detector using Vosk grammar decoding.
    """

    def __init__(
        self,
        model_path: str,
        wake_phrase: str = "hey yukti",
        samplerate: int = 16000
    ):
        self.model = vosk.Model(model_path)
        self.wake_phrase = wake_phrase.lower()
        self.samplerate = samplerate

        grammar = json.dumps([self.wake_phrase])
        self.rec = vosk.KaldiRecognizer(self.model, samplerate, grammar)

    def listen(self) -> bool:
        """
        Blocks until wake-word is detected.
        """
        with sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=4000,
            dtype="int16",
            channels=1
        ) as stream:
            while True:
                data, _ = stream.read(4000)
                if self.rec.AcceptWaveform(bytes(data)):
                    result = json.loads(self.rec.Result())
                    text = result.get("text", "").strip()
                    if text == self.wake_phrase:
                        return True
