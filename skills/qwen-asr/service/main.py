#!/usr/bin/env python3
"""
Qwen3-ASR-0.6B-4bit Speech Recognition Service
Uses HuggingFace MLX model for offline ASR on Apple Silicon
"""

import os
import sys
import time
import argparse
import tempfile
from pathlib import Path
from contextlib import asynccontextmanager

# Use ModelScope/HuggingFace mirror for faster downloads
if not os.environ.get("HF_ENDPOINT"):
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ.setdefault("HF_HOME", str(Path.home() / ".cache" / "huggingface"))

import httpx
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch

# Configuration
MODEL_ID = os.environ.get("QWEN_ASR_MODEL", "mlx-community/Qwen3-ASR-0.6B-4bit")
DEVICE = "mps" if sys.platform == "darwin" else "cpu"
DTYPE = torch.float16 if sys.platform == "darwin" else torch.float32

# Global pipeline
asr_pipeline = None


def load_model():
    """Load the ASR model into memory."""
    global asr_pipeline

    print(f"Loading model: {MODEL_ID}")
    print(f"   Device: {DEVICE}")

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        MODEL_ID,
        torch_dtype=DTYPE,
        low_cpu_mem_usage=True,
    )

    processor = AutoProcessor.from_pretrained(MODEL_ID)

    asr_pipeline = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=256,
        torch_dtype=DTYPE,
        device=DEVICE,
    )

    print("Model loaded!")
    return asr_pipeline


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load model on startup."""
    load_model()
    yield


app = FastAPI(
    title="Qwen3-ASR Service",
    description="Offline speech recognition using MLX on Apple Silicon",
    lifespan=lifespan
)


class ASRRequest(BaseModel):
    audio_url: str = None
    language: str = None
    return_timestamps: bool = False


class ASRResponse(BaseModel):
    text: str
    chunks: list = None
    processing_time: float


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "model": MODEL_ID}


@app.get("/info")
async def model_info():
    """Get model information."""
    return {
        "model": MODEL_ID,
        "device": DEVICE,
        "dtype": str(DTYPE)
    }


@app.post("/transcribe", response_model=ASRResponse)
async def transcribe_audio(request: ASRRequest = None, file: UploadFile = None):
    """
    Transcribe audio to text.

    Either provide:
    - audio_url: URL to audio file
    - file: Upload audio file directly
    """
    start_time = time.time()

    if asr_pipeline is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    temp_path = None
    try:
        if file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                content = await file.read()
                tmp.write(content)
                temp_path = tmp.name
            audio_path = temp_path
        elif request and request.audio_url:
            async with httpx.AsyncClient(timeout=60) as client:
                resp = await client.get(request.audio_url)
                resp.raise_for_status()
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(resp.content)
                    temp_path = tmp.name
            audio_path = temp_path
        else:
            raise HTTPException(status_code=400, detail="Provide audio_url or upload a file")

        result = asr_pipeline(
            audio_path,
            generate_kwargs={
                "language": request.language if request else None,
                "return_timestamps": request.return_timestamps if request else False,
            } if request else {}
        )

        processing_time = time.time() - start_time

        return ASRResponse(
            text=result["text"],
            chunks=result.get("chunks", None),
            processing_time=processing_time
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)


@app.post("/transcribe_url")
async def transcribe_url(audio_url: str, language: str = None):
    """Transcribe audio from URL."""
    return await transcribe_audio(ASRRequest(audio_url=audio_url, language=language))


def main():
    """Run as a standalone FastAPI server."""
    import uvicorn

    parser = argparse.ArgumentParser(description="Qwen3-ASR Service")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind")
    parser.add_argument("--port", type=int, default=8100, help="Port to bind")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")

    args = parser.parse_args()

    print(f"Starting Qwen3-ASR Service")
    print(f"   Endpoint: http://{args.host}:{args.port}")
    print(f"   API Docs: http://{args.host}:{args.port}/docs")

    uvicorn.run(app, host=args.host, port=args.port, reload=args.reload)


if __name__ == "__main__":
    main()
