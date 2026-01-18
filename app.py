# app.py  ✅ FINAL FULL WORKING CODE (OFFLINE WHISPER + OPENAI GPT)

import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import whisper

# ----------------- LOAD ENV -----------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Lecture Voice-to-Notes Generator")
st.title("🎤 Lecture Voice-to-Notes Generator")

# ----------------- OFFLINE TRANSCRIPTION -----------------
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

def transcribe_audio(audio_path):
    model = load_whisper_model()
    result = model.transcribe(audio_path)
    return result["text"]

# ----------------- TEXT GENERATION -----------------
def generate_text(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    return response.output_text

# ----------------- UI -----------------
uploaded_file = st.file_uploader(
    "Upload Lecture Audio (MP3 / WAV)",
    type=["mp3", "wav"]
)

if uploaded_file:
    audio_path = "lecture_audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(audio_path)
    st.success("Audio uploaded successfully")

    if st.button("Generate Notes"):
        with st.spinner("Transcribing audio..."):
            transcript = transcribe_audio(audio_path)

        with st.spinner("Generating study materials..."):
            notes = generate_text(
                f"Summarize the following lecture into clear study notes:\n{transcript}"
            )
            flashcards = generate_text(
                f"Create flashcards from these notes:\n{notes}"
            )
            quiz = generate_text(
                f"Create 5 MCQs with answers from these notes:\n{notes}"
            )

        st.subheader("📄 Transcript")
        st.write(transcript)

        st.subheader("📝 Study Notes")
        st.write(notes)

        st.subheader("🧠 Flashcards")
        st.write(flashcards)

        st.subheader("❓ Quiz")
        st.write(quiz)







