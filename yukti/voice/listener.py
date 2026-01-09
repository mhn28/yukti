import json
import vosk
import sounddevice as sd

SAMPLE_RATE = 16000
BLOCK_SIZE = 8000

def listen_with_grammar(model_path: str, grammar_path: str) -> str:
    model = vosk.Model(model_path)
    grammar = open(grammar_path).read()
    rec = vosk.KaldiRecognizer(model, SAMPLE_RATE, grammar)

    print("\n🎙️ Listening (grammar-constrained)… Speak clearly.\n")

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        dtype="int16",
        channels=1,
    ) as stream:
        while True:
            data, _ = stream.read(BLOCK_SIZE)
            if rec.AcceptWaveform(bytes(data)):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if text:
                    return text
