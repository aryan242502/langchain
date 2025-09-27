import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Supported translation models
translation_models = {
    ("English", "Hindi"): "Helsinki-NLP/opus-mt-en-hi",
    ("Hindi", "English"): "Helsinki-NLP/opus-mt-hi-en",
    ("English", "French"): "Helsinki-NLP/opus-mt-en-fr",
    ("French", "English"): "Helsinki-NLP/opus-mt-fr-en",
    ("English", "German"): "Helsinki-NLP/opus-mt-en-de",
    ("German", "English"): "Helsinki-NLP/opus-mt-de-en",
}

st.set_page_config(page_title="🌍 Multi-Language Translator", layout="centered")

st.title("🌍 Multi-Language Translator (Fast + Lightweight)")

from_lang = st.selectbox("From Language", ["English", "Hindi", "French", "German"])
to_lang = st.selectbox("To Language", ["English", "Hindi", "French", "German"])

text = st.text_area("🔥 Enter text to translate:")

if st.button("Translate"):
    if from_lang == to_lang:
        st.warning("⚠️ Please select different languages for translation.")
    elif (from_lang, to_lang) not in translation_models:
        st.error("❌ This language pair is not supported yet.")
    else:
        model_name = translation_models[(from_lang, to_lang)]
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)

        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated_tokens = model.generate(**inputs, max_length=256)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        st.success(f"✅ Translation: {translated_text}")
