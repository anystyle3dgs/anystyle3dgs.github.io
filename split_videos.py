#!/usr/bin/env python3
"""
Two-pass video pipeline for the AnyStyle carousel:

  Pass 1 — Normalize
    Re-encode every source video to a common 25 fps, write to
    ./supplementary/normalized/, convert timestamps accordingly,
    and save the updated paths + timestamps back to files.json.
    Also stores a "split_dir" key per entry (the carousel directory name).

  Pass 2 — Split
    For each normalized video, skip the intro segment (everything
    before timestamps[0]), then extract the remaining segments and
    crop each one into `rows` equal-height sub-clips.
    Output: ./supplementary/splits/<simplified_name>/{0,1,2,...}.mp4
    Files are indexed globally per video (segment-major, row-minor order).
"""

import json, os, re, subprocess, sys

TARGET_FPS = 25
NORM_DIR   = "./supplementary/normalized"
SPLITS_DIR = "./supplementary/splits"
FILES_JSON = "files.json"


def simplified_name(path):
    """
    Derive a short directory name from a video filename, e.g.:
      03_Stylos_vs_Anystyle_comparison.mp4  →  stylos_vs_anystyle
      01_Anystyle_re10k_image_vs_text.mp4   →  re10k_image_vs_text
    Rules (applied in order, case-insensitive):
      1. Strip extension
      2. Strip leading NN_ prefix
      3. Strip leading 'anystyle_' prefix
      4. Lowercase
    """
    name = os.path.splitext(os.path.basename(path))[0]
    name = re.sub(r"^\d+_", "", name)           # strip leading NN_
    name = re.sub(r"^anystyle_", "", name, flags=re.IGNORECASE)
    return name.lower()


def ffprobe(filename, show_entries):
    r = subprocess.run(
        ["ffprobe", "-v", "quiet", "-select_streams", "v:0",
         "-show_entries", show_entries,
         "-of", "default=noprint_wrappers=1:nokey=1", filename],
        capture_output=True, text=True, check=True,
    )
    return r.stdout.strip()


def load_json(path):
    with open(path) as f:
        content = f.read()
    content = re.sub(r",(\s*[\]}])", r"\1", content)
    return json.loads(content)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"  → saved {path}")


# ── Pass 1: normalize to TARGET_FPS ──────────────────────────────────────────

print(f"\n{'='*60}")
print(f"Pass 1 — re-encoding all videos to {TARGET_FPS} fps")
print(f"{'='*60}")

os.makedirs(NORM_DIR, exist_ok=True)
data = load_json(FILES_JSON)

for entry in data:
    src = entry["filename"]
    if not os.path.exists(src):
        print(f"WARNING: {src} not found — skipping", file=sys.stderr)
        continue

    fps_raw  = ffprobe(src, "stream=r_frame_rate")
    num, den = fps_raw.split("/")
    orig_fps = float(num) / float(den)

    dst = os.path.join(NORM_DIR, os.path.basename(src))
    print(f"\n  {src}")

    if os.path.abspath(src) == os.path.abspath(dst):
        print(f"  already normalized at {TARGET_FPS} fps — skipping re-encode")
        entry["split_dir"] = simplified_name(src)
        continue

    print(f"  original fps: {orig_fps:.4f}  →  {TARGET_FPS}")

    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "warning",
         "-i", src,
         "-vf", f"fps={TARGET_FPS}",
         "-c:v", "libx264", "-crf", "17", "-preset", "slow",
         "-movflags", "+faststart", "-an",
         dst],
        check=True,
    )

    entry["filename"]  = dst
    entry["split_dir"] = simplified_name(src)   # e.g. "stylos_vs_anystyle"

save_json(FILES_JSON, data)

# ── Pass 2: split into per-segment, per-row clips ────────────────────────────

print(f"\n{'='*60}")
print("Pass 2 — splitting into carousel clips")
print(f"{'='*60}")

for entry in data:
    filename   = entry["filename"]
    timestamps = entry["timestamps"]
    rows       = int(entry["rows"])
    clip_dir   = os.path.join(SPLITS_DIR, entry["split_dir"])

    if not os.path.exists(filename):
        print(f"WARNING: {filename} not found — skipping", file=sys.stderr)
        continue

    os.makedirs(clip_dir, exist_ok=True)

    dims          = ffprobe(filename, "stream=width,height").split("\n")
    width, height = int(dims[0]), int(dims[1])
    row_h         = height // rows

    # Skip intro (0 … timestamps[0]-1); keep timestamps[0], timestamps[1], …
    segments = [
        (timestamps[i], timestamps[i + 1] if i + 1 < len(timestamps) else None)
        for i in range(len(timestamps))
    ]

    print(f"\n  {filename}  {width}×{height}  rows={rows}  →  {clip_dir}/")

    idx = 0
    for seg_i, (start_frame, end_frame) in enumerate(segments):
        for row in range(rows):
            y   = row * row_h
            out = os.path.join(clip_dir, f"{idx}.mp4")

            crop = f"crop={width}:{row_h}:0:{y}"
            trim = (
                f"trim=start_frame={start_frame}:end_frame={end_frame},setpts=PTS-STARTPTS"
                if end_frame is not None else
                f"trim=start_frame={start_frame},setpts=PTS-STARTPTS"
            )

            print(f"    [{idx}]  seg {seg_i+1} row {row+1}  "
                  f"frames {start_frame}–{end_frame or 'end'}  y={y}  →  {out}")
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "warning",
                 "-i", filename,
                 "-vf", f"{trim},{crop}",
                 "-c:v", "libx264", "-crf", "17", "-preset", "slow",
                 "-movflags", "+faststart", "-an", out],
                check=True,
            )
            idx += 1

print("\nDone. Clips written to", SPLITS_DIR)
