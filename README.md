# AnyStyle — Project Webpage

Landing page for the paper **"AnyStyle: Single-Pass Multimodal Stylization for 3D Gaussian Splatting"**.

- Live site: https://anystyle3dgs.github.io
- arXiv: https://arxiv.org/abs/2602.04043
- Code: https://github.com/joaxkal/anystyle

---

## Repository layout

```
├── index.html                        # Single-file webpage (no build step)
├── paper.pdf                         # Paper PDF served directly
├── assets/
│   ├── teaser.jpg                    # Main teaser figure
│   ├── method.jpg                    # Architecture diagram
│   └── comparison.jpg                # Method comparison table (rasterised from tex/)
├── tex/
│   └── comparison.pdf                # Source PDF for the comparison table
├── supplementary/                    # Video materials (see below)
│   ├── 01_Anystyle_re10k_image_vs_text.mp4
│   ├── 02_Anystyle_re10k_natural_text_prompts.mp4
│   ├── 03_Stylos_vs_Anystyle_comparison.mp4
│   ├── normalized/                   # 25 fps re-encoded copies (auto-generated)
│   └── splits/                       # Per-segment, per-row carousel clips (auto-generated)
│       ├── re10k_image_vs_text/          0.mp4 … 17.mp4
│       ├── re10k_natural_text_prompts/   0.mp4 … 7.mp4
│       └── stylos_vs_anystyle_comparison/  0.mp4 … 11.mp4
├── files.json                        # Split configuration (updated in-place by the pipeline)
├── split_videos.py                   # Video processing pipeline (see below)
├── pyproject.toml                    # uv project — Python dependencies
└── uv.lock
```

---

## Reproducing the video carousel clips

### 1. Get the source videos

Download **supplementary.zip** from the OpenReview submission and extract the three `.mp4` files into `supplementary/`:

```
supplementary/
├── 01_Anystyle_re10k_image_vs_text.mp4
├── 02_Anystyle_re10k_natural_text_prompts.mp4
└── 03_Stylos_vs_Anystyle_comparison.mp4
```

### 2. Install dependencies

The pipeline requires Python ≥ 3.13, `ffmpeg`, and `ffprobe`.
Python packages are managed with [uv](https://docs.astral.sh/uv/):

```bash
# Install uv if needed
pip install uv

# Install Python dependencies into the project venv
uv sync
```

### 3. Run the pipeline

```bash
uv run split_videos.py
```

**What it does — two passes:**

| Pass | Input | Output |
|------|-------|--------|
| 1 — Normalize | Source `.mp4` files | `supplementary/normalized/*.mp4` re-encoded at 25 fps (H.264, CRF 17) |
| 2 — Split | Normalized files | `supplementary/splits/<name>/<idx>.mp4` — one clip per carousel slide/row |

`files.json` is updated in-place with the normalized file paths and a `split_dir` key used by the webpage.

**Split logic:**
- `timestamps` in `files.json` are frame numbers **at 25 fps**.
- The first segment (frames 0 → `timestamps[0]−1`) is the intro and is **discarded**.
- Each remaining segment is cropped vertically into `rows` equal-height sub-clips.
- Clips are named `0.mp4`, `1.mp4`, … in segment-major, row-minor order.

### 4. Regenerating the comparison table image

`assets/comparison.jpg` is rasterised from `tex/comparison.pdf` using ImageMagick:

```bash
magick -density 400 tex/comparison.pdf -quality 95 assets/comparison.jpg
```

---

## Viewing locally

No build step required. Open `index.html` directly in a browser, or serve with:

```bash
python3 -m http.server
```

Videos require a local server (browsers block autoplay over `file://`).

---

## Deploying

Push to the `main` branch. GitHub Pages serves from the repository root automatically.
Changes are live within ~1 minute.

---

## Tech stack

| Concern | Library / tool |
|---------|----------------|
| CSS framework | DaisyUI v5 + Tailwind CSS v4 (CDN, no build) |
| Carousel | Swiper.js v11 (CDN) |
| Icons | Font Awesome 6 (CDN) |
| Font | Plus Jakarta Sans (Google Fonts) |
| Video processing | ffmpeg / ffprobe |
| Python env | uv |
