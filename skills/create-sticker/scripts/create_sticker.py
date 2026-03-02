#!/usr/bin/env python3
"""
Create Sticker — Generate LINE-style stickers with background removal.
Uses Google Gemini native SDK for image generation.
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

# ── Config ──────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REFERENCE_IMAGE = SKILL_DIR / "assets" / "example-character.jpeg"

DEFAULT_MODEL = "gemini-3-pro-image-preview"

_sticker_dir = os.environ.get("STICKER_OUTPUT_DIR", str(Path.home() / "stickers"))
RAW_DIR = Path(_sticker_dir) / "raw"
OUTPUT_DIR = Path(_sticker_dir)

# Background color to remove
BG_COLOR = (217, 217, 217)  # actual color from API output
BG_TOLERANCE = 20  # color distance threshold

# ── Character prompt base ───────────────────────────────
# ⚠️ Example character setup — replace with your own character description.
CHARACTER_BASE = """Chibi sticker of the character in the reference image.
Keep the shading and rendering style of the reference (NOT flat coloring), but in chibi proportions (large head, small body, 2.5 head ratio).
MUST include the character's dark beret (exactly as shown in reference image) AND round thin gold-framed glasses. These two accessories are essential. Upper body framing. Thin delicate outlines.
Solid flat light gray background RGB(240,240,240). No extra decorations, no border."""

# ── Sticker ideas ───────────────────────────────────────
STICKER_IDEAS = [
    "waving hello cheerfully with big smile",
    "giving thumbs up with wink",
    "holding a magnifying glass investigating",
    "drinking bubble tea happily",
    "sleeping on desk with zzz",
    "typing on laptop intensely",
    "jumping with excitement arms raised",
    "crying dramatically with waterfall tears",
    "angry with puffed cheeks",
    "making heart shape with hands",
    "running late with toast in mouth",
    "reading a book deeply focused",
    "taking notes with sparkle eyes",
    "confused with question marks",
    "victory pose with both peace signs",
    "embarrassed covering face blushing",
    "pointing forward determinedly",
    "sitting and hugging knees shyly",
    "laughing so hard holding stomach",
    "shocked jaw drop with sweat drop",
]


def get_api_key() -> str:
    """Get GEMINI_API_KEY from environment, exit with guidance if not set."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print(
            "Error: GEMINI_API_KEY environment variable is not set.\n"
            "\n"
            "To configure:\n"
            "  1. Get an API key at https://aistudio.google.com/apikey\n"
            "  2. Add to your shell config:\n"
            '     echo \'export GEMINI_API_KEY="your-key-here"\' >> ~/.zshrc\n'
            "     source ~/.zshrc\n",
            file=sys.stderr,
        )
        sys.exit(1)
    return key


def sanitize_filename(desc: str) -> str:
    """Convert description to safe filename."""
    name = desc.lower().strip()
    name = name.replace(" ", "_")
    safe = "".join(c for c in name if c.isalnum() or c == "_")
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe.strip("_")[:60]


def generate_image(prompt: str, model: str, aspect: str, size: str):
    """Call Gemini API to generate sticker image. Returns PIL Image."""
    from google import genai
    from google.genai import types
    from PIL import Image

    client = genai.Client(api_key=get_api_key())

    contents = [prompt]

    if REFERENCE_IMAGE.exists():
        ref_img = Image.open(REFERENCE_IMAGE)
        contents.append(ref_img)
        print(f"  📎 Reference image: {REFERENCE_IMAGE.name}")
    else:
        print(f"  ⚠️  Reference image not found: {REFERENCE_IMAGE}", file=sys.stderr)

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect,
                image_size=size,
            ),
        ),
    )

    # Extract generated image from response
    for part in response.parts:
        img = part.as_image()
        if img is not None:
            return img

    # If no image found, show any text response for debugging
    for part in response.parts:
        if part.text is not None:
            print(f"  Model response: {part.text}", file=sys.stderr)

    raise RuntimeError("No image in Gemini response")


def remove_background(input_path: Path, output_path: Path, bg_color=BG_COLOR, tolerance=BG_TOLERANCE):
    """
    Remove solid gray background via flood fill from edges.
    Only removes gray pixels — preserves white (clothes, socks, hair, outline).
    """
    from PIL import Image
    import numpy as np
    from collections import deque

    img = Image.open(input_path).convert("RGBA")
    data = np.array(img)
    h, w = data.shape[:2]

    rgb = data[:, :, :3].astype(np.float64)

    # Match gray background only (NOT white — character has white clothes)
    bg1 = np.array(bg_color, dtype=np.float64)
    bg2 = np.array([240, 240, 240], dtype=np.float64)  # lighter gray variant

    diff1 = np.sqrt(np.sum((rgb - bg1) ** 2, axis=2))
    diff2 = np.sqrt(np.sum((rgb - bg2) ** 2, axis=2))

    gray_match = (diff1 < tolerance) | (diff2 < tolerance)

    # Also match white for flood fill — strip model's white border so we add our own consistent one
    white = np.array([255, 255, 255], dtype=np.float64)
    diff_white = np.sqrt(np.sum((rgb - white) ** 2, axis=2))
    fill_match = gray_match | (diff_white < 35)

    # Flood fill from edges — spread through gray + adjacent white
    visited = np.zeros((h, w), dtype=bool)
    bg_mask = np.zeros((h, w), dtype=bool)
    queue = deque()

    for x in range(w):
        for y in [0, h - 1]:
            if gray_match[y, x] and not visited[y, x]:
                queue.append((y, x))
                visited[y, x] = True
    for y in range(h):
        for x in [0, w - 1]:
            if gray_match[y, x] and not visited[y, x]:
                queue.append((y, x))
                visited[y, x] = True

    while queue:
        cy, cx = queue.popleft()
        bg_mask[cy, cx] = True
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and fill_match[ny, nx]:
                visited[ny, nx] = True
                queue.append((ny, nx))

    # Apply transparency
    data[bg_mask, 3] = 0

    # Anti-alias: soften boundary edges that are also grayish
    from scipy.ndimage import binary_dilation
    dilated = binary_dilation(bg_mask, iterations=1)
    boundary = dilated & ~bg_mask
    boundary_gray = boundary & (diff1 < tolerance * 1.5)
    data[boundary_gray, 3] = (data[boundary_gray, 3] * 0.3).astype(np.uint8)

    result = Image.fromarray(data, "RGBA")

    # --- Post-processing: white outline + center & fill ---
    result = _outline_center_fill(result)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(output_path, format="PNG")
    print(f"  ✂️  Background removed → {output_path}")
    return output_path


def _outline_center_fill(img, stroke_px=12):
    """
    1. Add 12px white outline
    2. Center on canvas and scale up until edges touch boundary
    """
    from PIL import Image, ImageFilter
    from scipy.ndimage import binary_dilation
    import numpy as np

    w, h = img.size

    # Add white outline
    alpha = np.array(img.split()[3])
    mask = alpha > 128
    dilated = binary_dilation(mask, iterations=stroke_px)
    outline_mask = dilated & ~mask

    outline = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    arr = np.array(outline)
    arr[outline_mask] = [255, 255, 255, 255]
    outline = Image.fromarray(arr, "RGBA").filter(ImageFilter.GaussianBlur(radius=1))

    composed = Image.alpha_composite(outline, img)
    print(f"  🖊️  Added {stroke_px}px white outline")

    # Find content bounding box
    composed_alpha = np.array(composed.split()[3])
    rows = np.any(composed_alpha > 10, axis=1)
    cols = np.any(composed_alpha > 10, axis=0)
    if not rows.any() or not cols.any():
        return composed

    top, bottom = np.where(rows)[0][[0, -1]]
    left, right = np.where(cols)[0][[0, -1]]

    content_w = right - left + 1
    content_h = bottom - top + 1

    # If content doesn't touch edges, center and scale up
    margin = 4  # small safety margin in px
    if left > margin or top > margin or (w - right - 1) > margin or (h - bottom - 1) > margin:
        cropped = composed.crop((left, top, right + 1, bottom + 1))
        scale = min((w - margin * 2) / content_w, (h - margin * 2) / content_h)
        new_w = int(content_w * scale)
        new_h = int(content_h * scale)
        scaled = cropped.resize((new_w, new_h), Image.LANCZOS)

        canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        paste_x = (w - new_w) // 2
        paste_y = (h - new_h) // 2
        canvas.paste(scaled, (paste_x, paste_y))
        print(f"  📐 Centered & scaled {scale:.2f}x ({content_w}x{content_h} → {new_w}x{new_h})")
        return canvas

    return composed


def main():
    parser = argparse.ArgumentParser(description="Generate LINE-style character stickers")
    parser.add_argument("description", nargs="?", help="Sticker action/pose description in English")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--no-remove-bg", action="store_true", help="Skip background removal")
    parser.add_argument("--ideas", action="store_true", help="Print sticker ideas")
    parser.add_argument("--tolerance", type=int, default=BG_TOLERANCE, help="BG removal color tolerance")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--aspect", default="1:1", help="Aspect ratio (default: 1:1)")
    parser.add_argument("--size", default="2K", help="Image size: 512px, 1K, 2K, 4K (default: 2K)")
    args = parser.parse_args()

    if args.ideas:
        print("🎨 Sticker ideas:")
        for i, idea in enumerate(STICKER_IDEAS, 1):
            print(f"  {i:2d}. {idea}")
        return

    if not args.description:
        print("Usage: create_sticker.py \"sticker description\"", file=sys.stderr)
        print("       create_sticker.py --ideas", file=sys.stderr)
        sys.exit(1)

    desc = args.description
    filename = sanitize_filename(desc)
    if not filename:
        filename = f"sticker_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    print(f"🎨 Generating sticker: {desc}")
    prompt = f"{CHARACTER_BASE}\nAction/Pose: {desc}"

    # 1. Generate
    print(f"  🖌️  Calling Gemini ({args.model})...")
    generated_img = generate_image(prompt, model=args.model, aspect=args.aspect, size=args.size)
    print(f"  ✅ Generated!")

    # 2. Save raw
    raw_path = RAW_DIR / f"{filename}.png"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    generated_img.save(raw_path, format="PNG")
    print(f"  💾 Raw saved: {raw_path}")

    # 3. Remove background
    if not args.no_remove_bg:
        final_path = args.output_dir / f"{filename}.png"
        try:
            remove_background(raw_path, final_path, tolerance=args.tolerance)
        except ImportError as e:
            print(f"  ⚠️  BG removal needs dependencies: {e}", file=sys.stderr)
            print(f"  💡 Install: pip install numpy scipy Pillow", file=sys.stderr)
            print(f"  📁 Raw image available at: {raw_path}")
            final_path = raw_path
    else:
        final_path = raw_path

    print(f"\n✅ Sticker ready: {final_path}")
    print(f"MEDIA:{final_path}")


if __name__ == "__main__":
    main()
