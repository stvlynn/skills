#!/usr/bin/env python3
"""
Qwen TTS Generator - Qwen3-TTS CustomVoice (MLX)

Generates speech audio files with organized output and automatic cleanup.

Usage:
    python tts.py "Text to speak" [--speaker SERENA] [--instruct INSTRUCT] [--speed SPEED]

Output:
    Files saved to: ~/tts-output/ (or $QWEN_TTS_OUTPUT_DIR)
    Files older than 24 hours are automatically cleaned up.
"""
import argparse
import os
import sys
import glob
from datetime import datetime, timedelta

# Use ModelScope mirror for faster downloads in China
if not os.environ.get("HF_ENDPOINT"):
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

import numpy as np
from mlx_audio.tts.utils import load_model
import soundfile as sf

# Configuration
TTS_DIR = os.environ.get("QWEN_TTS_OUTPUT_DIR", os.path.expanduser("~/tts-output"))
DEFAULT_MODEL = os.environ.get("QWEN_TTS_MODEL", "mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-4bit")
# ⚠️ 以下为示例默认值，请根据实际使用场景修改
DEFAULT_SPEAKER = "Serena"
DEFAULT_INSTRUCT = "撒娇语气"
DEFAULT_LANGUAGE = "Chinese"
DEFAULT_SPEED = 1.0
MAX_FILE_AGE_HOURS = 24


def setup_output_dir():
    """Create output directory if it doesn't exist."""
    os.makedirs(TTS_DIR, exist_ok=True)
    return TTS_DIR


def cleanup_old_files():
    """Remove audio files older than MAX_FILE_AGE_HOURS."""
    cutoff = datetime.now() - timedelta(hours=MAX_FILE_AGE_HOURS)
    cleaned = 0

    for filepath in glob.glob(os.path.join(TTS_DIR, "tts_*.wav")):
        try:
            mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
            if mtime < cutoff:
                os.remove(filepath)
                cleaned += 1
        except OSError:
            pass

    if cleaned > 0:
        print(f"Cleaned up {cleaned} old audio files")

    return cleaned


def generate_timestamp():
    """Generate unique timestamp for filenames."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_model():
    """Load and cache the TTS model."""
    if not hasattr(get_model, "_model"):
        print(f"Loading model: {DEFAULT_MODEL}")
        get_model._model = load_model(DEFAULT_MODEL)
        print("Model loaded!")
        print(f"   Supported speakers: {get_model._model.get_supported_speakers()}")
    return get_model._model


def generate_speech(
    text: str,
    speaker: str = DEFAULT_SPEAKER,
    instruct: str = DEFAULT_INSTRUCT,
    language: str = DEFAULT_LANGUAGE,
    speed: float = DEFAULT_SPEED,
    output_dir: str = None
) -> str:
    """
    Generate speech audio file.

    Args:
        text: The text to synthesize
        speaker: Voice speaker name (default: Serena)
        instruct: Emotion/instruction (default: 撒娇语气)
        language: Language (default: Chinese)
        speed: Speech speed (default: 1.0)
        output_dir: Output directory (default: TTS_DIR)

    Returns:
        Path to the generated audio file
    """
    if output_dir is None:
        output_dir = setup_output_dir()
    else:
        os.makedirs(output_dir, exist_ok=True)

    # Cleanup old files before generation
    cleanup_old_files()

    # Load model
    model = get_model()

    # Generate timestamp for filename
    timestamp = generate_timestamp()

    print(f"\nGenerating speech...")
    print(f"   Text: {text[:50]}{'...' if len(text) > 50 else ''}")
    print(f"   Speaker: {speaker}")
    print(f"   Instruct: {instruct}")
    print(f"   Language: {language}")
    print(f"   Speed: {speed}x")

    # Generate audio using generate_custom_voice
    results = model.generate_custom_voice(
        text=text,
        speaker=speaker,
        language=language,
        instruct=instruct,
    )

    # Save the first result
    output_file = os.path.join(output_dir, f"tts_{timestamp}_000.wav")

    for i, result in enumerate(results):
        audio_np = np.array(result.audio)
        sf.write(output_file, audio_np, model.sample_rate)

        print(f"\nSaved: {output_file}")
        print(f"   Duration: {len(audio_np) / model.sample_rate:.2f}s")
        print(f"   Sample rate: {model.sample_rate}Hz")
        break  # Only save first result

    return output_file


def main():
    parser = argparse.ArgumentParser(
        description="Qwen TTS Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tts.py "你好！"
  python tts.py "Hello!" --speaker Ryan --language English
  python tts.py "其实我真的有发现..." --instruct 冷静分析 --speed 1.1
        """
    )

    parser.add_argument("text", help="Text to synthesize")
    parser.add_argument("--speaker", default=DEFAULT_SPEAKER,
                        help=f"Voice speaker (default: {DEFAULT_SPEAKER})")
    parser.add_argument("--instruct", default=DEFAULT_INSTRUCT,
                        help=f"Emotion/instruction (default: {DEFAULT_INSTRUCT})")
    parser.add_argument("--language", default=DEFAULT_LANGUAGE,
                        help=f"Language (default: {DEFAULT_LANGUAGE})")
    parser.add_argument("--speed", type=float, default=DEFAULT_SPEED,
                        help=f"Speech speed (default: {DEFAULT_SPEED})")
    parser.add_argument("--output", "-o", default=None,
                        help=f"Output directory (default: {TTS_DIR})")
    parser.add_argument("--no-cleanup", action="store_true",
                        help="Skip automatic cleanup of old files")

    args = parser.parse_args()

    # Setup output directory
    setup_output_dir()

    # Generate speech
    output_file = generate_speech(
        text=args.text,
        speaker=args.speaker,
        instruct=args.instruct,
        language=args.language,
        speed=args.speed,
        output_dir=args.output
    )

    print(f"\nFile: {output_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
