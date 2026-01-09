from yukti.voice.input import VoiceInput
from yukti.voice.grammar import enforce_statistics_grammar
from yukti.runtime.confirm import confirm_text
from yukti.llm.runtime import invoke_llm
from yukti.persona.state import enable_persona

MODEL_PATH = "models/vosk-model-en-us-0.22"

def run():
    enable_persona()

    print("\\n🎙️ Speak your statistics question...\\n")

    v = VoiceInput(model_path=MODEL_PATH)
    raw = v.listen_once(timeout=8)

    if not raw or not raw.strip():
        print("❌ No speech detected.")
        return

    constrained = enforce_statistics_grammar(raw)
    print(f"\\n📝 Recognized (grammar-constrained):\\n{constrained}\\n")

    final = confirm_text(constrained)
    if final is None:
        print("🔁 Cancelled by user.")
        return

    print("\\n📊 Sending to Yukti (statistics-only mode)...\\n")
    invoke_llm(final)

if __name__ == "__main__":
    run()
