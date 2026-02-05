

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

SUPPORTED_LANGUAGES = {
    "hindi": sanscript.DEVANAGARI,
    "bengali": sanscript.BENGALI,
    "tamil": sanscript.TAMIL
}

def transliterate_text(text: str, target_language: str) -> str:
    target_language = target_language.lower()

    if target_language not in SUPPORTED_LANGUAGES:
        return f"Error: Unsupported language. Choose from {list(SUPPORTED_LANGUAGES.keys())}"

    result = transliterate(
        text,
        sanscript.ITRANS,   # Roman input
        SUPPORTED_LANGUAGES[target_language]
    )
    return result


if __name__ == "__main__":
    print("=== Transliteration Tool ===")
    print("Supported languages: Hindi, Bengali, Tamil\n")

    input_text = input("Enter text (Roman English): ").strip()
    language = input("Target language: ").strip()

    output = transliterate_text(input_text, language)

    print("\n--- Output ---")
    print(output)
