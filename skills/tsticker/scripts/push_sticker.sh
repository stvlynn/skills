#!/bin/bash
# Push a single sticker to an existing tsticker pack
# Usage: push_sticker.sh <image_path> <pack_dir> [emoji]
set -e
IMAGE="$1"
PACK_DIR="${2:-$HOME/Pictures/lynn-stickers}"
EMOJI="$3"
if [ -z "$IMAGE" ]; then echo 'Usage: push_sticker.sh <image> [pack_dir] [emoji]'; exit 1; fi
if [ ! -f "$IMAGE" ]; then echo "Image not found: $IMAGE"; exit 1; fi
if [ ! -d "$PACK_DIR/stickers" ]; then echo "Pack not found: $PACK_DIR"; exit 1; fi
BASENAME=$(basename "$IMAGE")
if [ -n "$EMOJI" ]; then DEST="$PACK_DIR/stickers/${EMOJI}${BASENAME}"; else DEST="$PACK_DIR/stickers/$BASENAME"; fi
cp "$IMAGE" "$DEST"
echo "Copied: $DEST"
cd "$PACK_DIR"
tsticker push
