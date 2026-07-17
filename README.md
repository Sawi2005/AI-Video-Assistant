# AI Video Assistant

## Overview

AI Video Assistant is an AI-powered application that transforms YouTube videos, meeting recordings, lectures, and podcasts into a searchable knowledge base. It automatically generates transcripts, professional summaries, action items, key decisions, unresolved questions, and enables users to interact with the content through an intelligent chat interface powered by Retrieval-Augmented Generation (RAG).

The project demonstrates an end-to-end Generative AI pipeline, integrating speech-to-text, large language models, vector databases, and semantic search to simplify video understanding and information retrieval.

---

## Features

- Analyze YouTube videos or local audio/video files
- Automatic multilingual transcription
  - English using Whisper
  - Hindi/Hinglish using Sarvam AI Speech-to-Text
- Generate concise professional summaries
- Extract action items with owners and deadlines
- Identify key decisions made in meetings or videos
- Detect open or unresolved questions
- Chat with the transcript using Retrieval-Augmented Generation (RAG)
- Transparent fallback to general knowledge when transcript information is unavailable
- Interactive Streamlit dashboard with live processing status and chat interface

---

## Project Workflow

1. Accept a YouTube URL or local audio/video file.
2. Download or process the media file.
3. Convert audio into suitable chunks.
4. Transcribe speech using Whisper or Sarvam AI.
5. Generate a concise summary using Mistral AI.
6. Extract action items, decisions, and open questions.
7. Create embeddings using HuggingFace models.
8. Store transcript embeddings in a Chroma Vector Database.
9. Retrieve relevant transcript chunks using semantic search.
10. Generate context-aware answers through an AI-powered chat interface.

---

## Technologies Used

### Programming Language
- Python

### AI & Large Language Models
- Mistral AI
- LangChain

### Speech-to-Text
- Whisper
- Sarvam AI

### Vector Database
- ChromaDB

### Embedding Model
- HuggingFace all-MiniLM-L6-v2

### Audio Processing
- yt-dlp
- pydub
- FFmpeg

### Frontend
- Streamlit

### Environment Management
- python-dotenv

---

## Project Structure

```
AI-Video-Assistant/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
│
├── core/
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── extractor.py
│   ├── vector_store.py
│   └── rag_engine.py
│
├── utils/
│   └── audio_processor.py
│
├── downloads/
├── vector_db/
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Video-Assistant.git

cd AI-Video-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install FFmpeg and ensure it is added to your system PATH.

---

## Configuration

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key

SARVAM_API_KEY=your_sarvam_api_key

WHISPER_MODEL=small

YTDLP_COOKIES_FROM_BROWSER=chrome
```

---

## Usage

Run the Streamlit application

```bash
streamlit run app.py
```

Or run the command-line version

```bash
python main.py
```

---

## Applications

- Meeting summarization
- Lecture and course notes generation
- YouTube content analysis
- Podcast summarization
- Knowledge management
- AI-powered document search
- Team collaboration and meeting tracking

---

## Future Enhancements

- Speaker diarization
- Timestamp-based citations
- Multi-language subtitle generation
- Export summaries as PDF or DOCX
- Voice-based AI assistant
- Cloud storage integration
- Video highlight generation
- Support for additional languages

---

## Known Limitations

- Longer videos require more processing time.
- YouTube downloads may require authentication cookies in some cases.
- Chat responses are dependent on transcript quality and accuracy.


---
