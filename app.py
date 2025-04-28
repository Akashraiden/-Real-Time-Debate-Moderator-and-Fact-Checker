import streamlit as st
import whisper
import google.generativeai as genai
import os
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set Streamlit page configurations
st.set_page_config(
    page_title="🎤 Real-Time Debate Moderator & Fact-Checker",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎤 Real-Time Debate Moderator & Fact-Checker")
st.write("Upload debate conversation to transcribe, moderate, fact-check claims, and analyze sentiment in multiple languages.")

# Load Whisper and Gemini models
@st.cache_resource
def load_models():
    whisper_model = whisper.load_model("base")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)

    # Use the Gemini 1.5 Pro model for text tasks (summarization and translation)
    gemini_model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

    return whisper_model, gemini_model

whisper_model, gemini_model = load_models()

# Send text to Gemini for a specific task
def query_gemini(task_prompt, text):
    try:
        response = gemini_model.generate_content(f"{task_prompt}: {text}")
        return response.text
    except Exception as e:
        st.error(f"Gemini error: {str(e)}")
        return None

# Upload Section
st.subheader("📁 Upload an Audio File")
uploaded_audio = st.file_uploader("Choose an audio file", type=["mp3", "wav", "ogg"])

if uploaded_audio:
    file_ext = uploaded_audio.name.split(".")[-1]
    with NamedTemporaryFile(suffix=f".{file_ext}", delete=False) as tmp:
        tmp_path = tmp.name
        tmp.write(uploaded_audio.read())
        tmp.flush()

    st.audio(tmp_path, format=f"audio/{file_ext}")

    with st.spinner("Transcribing uploaded audio..."):
        try:
            transcription = whisper_model.transcribe(tmp_path)["text"]
            st.write(f"Transcription: {transcription}")
        except Exception as e:
            st.error(f"Error during transcription: {str(e)}")

    st.subheader("AI Tasks")

    # Real-time Debate Moderation
    if st.button("Moderate Debate"):
        st.write(query_gemini("Moderate the debate and ensure it's on-topic and respectful", transcription))

    # Fact-Checking
    if st.button("Fact-Check the Statement"):
        st.write(query_gemini("Is the following statement true? [fact-based claim]", transcription))

    # Sentiment Analysis
    sentiment_language = st.selectbox("Select Language for Sentiment Analysis", ["English", "Spanish", "French", "German", "Chinese", "Japanese"])
    if st.button(f"Analyze Sentiment in {sentiment_language}"):
        sentiment_prompt = f"Analyze the sentiment of the following text in {sentiment_language}. Is it positive, negative, or neutral?"
        st.write(query_gemini(sentiment_prompt, transcription))

    # Summarization
    if st.button("Summarize the Text"):
        st.write(query_gemini("Summarize the following text", transcription))

    # Translation
    translation_language = st.selectbox("Select Language for Translation", ["English", "Spanish", "French", "German", "Chinese", "Japanese"])
    if st.button(f"Translate to {translation_language}"):
        translation_prompt = f"Translate the following text into {translation_language}: {transcription}"
        st.write(query_gemini("Translation Task", translation_prompt))

    try:
        os.unlink(tmp_path)             
    except Exception as e:                          
        st.warning(f"Could not delete file: {str(e)}")

st.caption("Note: This demo uses your Gemini API key. In production, store keys securely using secrets or environment variables.")
