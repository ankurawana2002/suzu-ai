
import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

st.set_page_config(page_title="Suzu - Talking AI", page_icon="👧", layout="centered")

st.markdown("<h1 style='text-align: center; color: #d63384;'>Suzu - AI for Kids</h1>", unsafe_allow_html=True)
st.image("suzu_image.webp", width=300)

user_input = st.text_input("Kya aap Suzu se baat karna chahenge?")

def speak(text):
    tts = gTTS(text)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_base64 = base64.b64encode(fp.read()).decode("utf-8")
    audio_html = f'<audio autoplay="true" controls="controls"><source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3" /></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

if st.button("Suzu se Suno"):
    if user_input.strip():
        reply = f"Namaste! Main Suzu hoon. Aapne kaha: {user_input}"
        st.write("🗣️ Suzu: " + reply)
        speak(reply)
    else:
        st.warning("Pehle kuch likhiye jisse Suzu jawab de sake 😊")
