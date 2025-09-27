import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer, pipeline

# -------------------------
# 🌍 Supported languages
# -------------------------
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt"
}

# -------------------------
# ⚙️ Load Model + Tokenizer
# -------------------------
@st.cache_resource
def load_translator():
    model_name = "facebook/m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    translator = pipeline("translation", model=model, tokenizer=tokenizer)
    return translator, tokenizer

translator, tokenizer = load_translator()

# -------------------------
# 🎨 Streamlit UI
# -------------------------
st.set_page_config(page_title="🌍 Multi-Language Translator", layout="centered")
st.title("🌍 Multi-Language Translator (M2M100 + Streamlit)")

src_lang = st.selectbox("From Language", list(LANGUAGES.keys()))
tgt_lang = st.selectbox("To Language", list(LANGUAGES.keys()))

text = st.text_area("✍️ Enter text to translate:", "")

if st.button("Translate"):
    if text.strip():
        tokenizer.src_lang = LANGUAGES[src_lang]
        encoded = tokenizer(text, return_tensors="pt")
        generated_tokens = translator.model.generate(
            **encoded, forced_bos_token_id=tokenizer.get_lang_id(LANGUAGES[tgt_lang])
        )
        result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        st.success(f"✅ Translation:\n\n{result}")
    else:
        st.warning("⚠️ Please enter some text to translate.")
