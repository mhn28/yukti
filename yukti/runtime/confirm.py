def confirm_text(text: str) -> str:
    print("\n📝 Recognized text:\n")
    print(f"  {text}\n")
    choice = input("Send to Yukti? [y = send / e = edit / n = cancel]: ").strip().lower()

    if choice == "y":
        return text
    if choice == "e":
        return input("\n✏️ Edit text:\n> ").strip()
    return ""
