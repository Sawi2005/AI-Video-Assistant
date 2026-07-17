from dotenv import load_dotenv
load_dotenv()

import yt_dlp
from pydub import AudioSegment
import os

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR,exist_ok = True)

# --- Cookie / bot-check workaround -----------------------------------------
# YouTube sometimes responds with "Sign in to confirm you're not a bot" for
# requests that don't look like they come from a logged-in browser session.
# Fix: attach real cookies to the yt-dlp request, either by pointing at a
# browser you're logged into YouTube with, or a cookies.txt file exported
# from one (e.g. via the "Get cookies.txt" browser extension).
#
# Configure ONE of these via environment variables (.env):
#   YTDLP_COOKIES_FROM_BROWSER=chrome        # or firefox, edge, brave, etc.
#   YTDLP_COOKIES_FILE=/path/to/cookies.txt  # exported Netscape-format file
COOKIES_FROM_BROWSER = os.getenv("YTDLP_COOKIES_FROM_BROWSER")  # e.g. "chrome"
COOKIES_FILE = os.getenv("YTDLP_COOKIES_FILE")  # e.g. "cookies.txt"


def download_youtube_audio(url: str)->str:
    # place to store the brought audio file
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")
    # yt config
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,

        "ffmpeg_location": r"C:\Users\rakes\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin",

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        # "quiet": True,
    }

    # Attach cookies if configured — this is what resolves the
    # "Sign in to confirm you're not a bot" error in most cases.
    if COOKIES_FROM_BROWSER:
        ydl_opts["cookiesfrombrowser"] = (COOKIES_FROM_BROWSER,)
    elif COOKIES_FILE:
        ydl_opts["cookiefile"] = COOKIES_FILE

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav")
        return filename
    except yt_dlp.utils.DownloadError as e:
        if "Sign in to confirm" in str(e):
            raise RuntimeError(
                "YouTube is blocking this download as bot traffic. Fix by setting "
                "YTDLP_COOKIES_FROM_BROWSER=chrome (or firefox/edge/brave) in your .env "
                "file — with that browser logged into YouTube and closed while running this — "
                "or export cookies.txt from your browser and set YTDLP_COOKIES_FILE instead."
            ) from e
        raise

def convert_to_wav(input_path: str) -> str:
    """Convert any audio/video file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    # auto detects type of file
    audio = AudioSegment.from_file(input_path)
    # sets channel to monoaudio 
    audio = audio.set_channels(1).set_frame_rate(16000) #16khz
    audio.export(output_path, format="wav")
    return output_path

def chunk_audio(wav_path : str , chunk_minutes : int = 10) -> list:
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes * 60 * 1000 

    chunks = []

    # audio length is in milli sec and at every certail 10 mins chunks are performed
    for i, start in enumerate(range(0,len(audio),chunk_ms)):
        chunk = audio[start : start + chunk_ms]
        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path , format = "wav")

        chunks.append(chunk_path)
    
    return chunks

def process_input(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):
        print("Detected YouTube URL. Downloading audio...")
        wav_path = download_youtube_audio(source)
    else:
        print("Detected local file. Converting to WAV...")
        wav_path = convert_to_wav(source)

    print("Chunking audio...")
    chunks = chunk_audio(wav_path)
    print(f"Audio ready — {len(chunks)} chunk(s) created.")
    return chunks