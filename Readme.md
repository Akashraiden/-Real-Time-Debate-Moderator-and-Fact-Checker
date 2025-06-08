# 🎤 Real-Time Debate Moderator & Fact-Checker

This Streamlit application enables users to **transcribe**, **moderate**, **fact-check**, **analyze sentiment**, **summarize**, and **translate** audio content from live or recorded debates. It leverages **OpenAI's Whisper** for audio transcription and **Gemini 1.5 Pro** (Google Generative AI) for intelligent text-based tasks.

Whether you're analyzing a political debate, educational discussion, or any conversation involving critical dialogue, this tool helps streamline insight extraction in real time.

---

## 🚀 Features

- 🎙️ **Real-Time Transcription** – Convert audio debates into accurate text using OpenAI Whisper.
- 📌 **Debate Moderation** – Detect off-topic or disrespectful content and highlight moderation suggestions.
- ✅ **Fact-Checking** – Validate factual claims using Gemini AI's reasoning capabilities.
- 😃 **Sentiment Analysis** – Identify tone (positive, negative, or neutral) in multiple languages.
- 📝 **Summarization** – Get a concise summary of long conversations or discussions.
- 🌍 **Multilingual Translation** – Translate debate transcripts into supported languages.

---

## 🛠️ Tech Stack

| Component         | Library / Service             |
|------------------|-------------------------------|
| Frontend UI      | [Streamlit](https://streamlit.io) |
| Transcription    | [Whisper](https://github.com/openai/whisper) |
| AI Text Tasks    | [Gemini 1.5 Pro](https://ai.google.dev/) |
| Env Management   | `python-dotenv`               |
| Containerization | Docker                         |
| Cloud Hosting    | AWS EC2                        |

---

## 📦 Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/real-time-debate-moderator.git
cd real-time-debate-moderator
