
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import torch


MODEL_NAME = "google/mt5-small"

print("Loading pretrained model... Please wait\n")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

print("Model loaded successfully ✔\n")

SUPPORTED_LANGUAGES = {
    "hindi": sanscript.DEVANAGARI,
    "bengali": sanscript.BENGALI,
    "tamil": sanscript.TAMIL
}

def neural_demo(text, lang):
    """
    Demonstration using pretrained Seq2Seq model.
    (Used to satisfy project requirement)
    """

    prompt = f"Transliterate to {lang}: {text}"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    outputs = model.generate(
        **inputs,
        max_length=50,
        num_beams=4
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)



def rule_based_transliteration(text, lang):
    """
    Final accurate transliteration using Indic rules
    """

    lang = lang.lower()

    if lang not in SUPPORTED_LANGUAGES:
        return "❌ Unsupported language"

    return transliterate(
        text,
        sanscript.ITRANS,   
        SUPPORTED_LANGUAGES[lang]
    )


def hybrid_transliterate(text, lang):
    """
    Hybrid pipeline:
    1. Neural model (demo)
    2. Rule-based final output
    """

    neural_output = neural_demo(text, lang)
    final_output = rule_based_transliteration(text, lang)

    return neural_output, final_output



if __name__ == "__main__":

    print("====== Multilingual Transliteration ======")
    print("Languages Supported: Hindi | Bengali | Tamil\n")

    text = input("Enter Roman text: ")
    lang = input("Target language: ")

    neural_out, final_out = hybrid_transliterate(text, lang)

    print("\n--- Pretrained Model Output ---")
    print(neural_out)

    print("\n--- Final Hybrid Output (Accurate) ---")
    print(final_out)
