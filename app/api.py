from fastapi import FastAPI, Body
import tempfile
from app.models.stt import transcribe_audio
from app.models.model import generate_response
app = FastAPI(title="Speech to Text API")

@app.post("/speech-to-text")
async def speech_to_text(audio_bytes: bytes = Body(...)):
    # Save runtime audio temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    text = transcribe_audio(tmp_path)

    return {
        "transcription": text
    }

@app.get("/generate-response")
async def get_response(prompt: str):
    response = await generate_response(prompt)
    return {
        "response": response
    }