import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="🌍 Multi-Language Translator", layout="centered")
st.title("🌍 Multi-Language Translator (Fast + Easy)")

# Supported languages (can add more)
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Japanese": "ja",
    "Chinese": "zh-cn",
}

# Dropdowns for selecting languages
from_lang = st.selectbox("From Language", list(languages.keys()))
to_lang = st.selectbox("To Language", list(languages.keys()))

# Input text
text = st.text_area("🔥 Enter text to translate:")

# Translate button
if st.button("Translate"):
    if from_lang == to_lang:
        st.warning("⚠️ Please select different languages.")
    elif text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[from_lang],
                target=languages[to_lang]
            ).translate(text)
            st.success(f"✅ Translation: {translated}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

