import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException

st.set_page_config(
    page_title="CodeAlpha Language Translator",
    page_icon="🌐",
    layout="centered",
)

LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Bengali": "bn",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Russian": "ru",
    "Korean": "ko",
    "Italian": "it",
}

st.title("🌐 Language Translation Tool")
st.caption("CodeAlpha Artificial Intelligence Internship — Task 1")
st.write("Enter text, choose languages, and translate it online.")

source_name = st.selectbox(
    "Translate from",
    list(LANGUAGES.keys()),
    index=0,
)
target_options = [name for name in LANGUAGES if name != "Auto Detect"]
target_name = st.selectbox("Translate to", target_options, index=1)

source_text = st.text_area(
    "Text to translate",
    placeholder="Type or paste your text here...",
    height=160,
    max_chars=5000,
)

if st.button("Translate", type="primary", use_container_width=True):
    if not source_text.strip():
        st.warning("Please enter some text before translating.")
    elif source_name == target_name:
        st.info("Choose two different languages.")
    else:
        try:
            source_code = LANGUAGES[source_name]
            target_code = LANGUAGES[target_name]
            translator = GoogleTranslator(
                source=source_code,
                target=target_code,
            )
            with st.spinner("Translating..."):
                translated_text = translator.translate(source_text.strip())

            if translated_text:
                st.subheader("Translated text")
                st.text_area(
                    "Result",
                    value=translated_text,
                    height=160,
                    key="translation_result",
                )
                st.download_button(
                    "Download translation as TXT",
                    data=translated_text,
                    file_name="translation.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
            else:
                st.error("No translation was returned. Please try again.")
        except LanguageNotSupportedException:
            st.error("That language combination is not supported.")
        except Exception as error:
            st.error(
                "Translation failed. Check your internet connection and "
                "try again. If the problem continues, the translation "
                "service may be temporarily unavailable."
            )
            with st.expander("Technical details"):
                st.code(str(error))

st.divider()
st.caption(
    "Demo project for learning. Translation requires internet access "
    "and uses the Google Translate service through deep-translator. "
    "Do not submit confidential text."
)
