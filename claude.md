# AnyStyle Landing Page - Development Notes

## Project Overview
This is the landing page for the AnyStyle research paper: "Single-Pass Multimodal Stylization for 3D Gaussian Splatting". The page is hosted on GitHub Pages and serves as the primary web presence for the paper.

**Paper Details:**
- arXiv: 2602.04043
- GitHub: https://github.com/joaxkal/anystyle
- Authors: Joanna Kaleta, Bartosz Świrta, Kacper Kania, Przemysław Spurek, Marek Kowalski

## Technology Stack

### Framework: DaisyUI + Tailwind CSS
**Why DaisyUI?**
- Built on Tailwind CSS with beautiful pre-designed components
- Modern, aesthetic design perfect for showcasing research
- Lightweight (42KB compressed)
- No build process needed (CDN-based)
- Responsive by default
- Easy to integrate with Font Awesome

**CDN Resources:**
- DaisyUI v5: `https://cdn.jsdelivr.net/npm/daisyui@5`
- Tailwind Browser: `https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4`
- Font Awesome 6: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css`
- Google Fonts (Plus Jakarta Sans): Modern, elegant sans-serif typography

### Theme & Color Scheme
- Using DaisyUI light theme as base (`data-theme="light"`)
- **Design Philosophy**: Truly minimalistic - clean and simple
  - White hero background with subtle border
  - Black, white, and gray color palette only
  - No colorful gradients or accents
  - Focus on typography and content
  - Outline buttons for minimal visual weight
  - Simple hover effects (no scale transforms)

### Typography
- **Font**: Plus Jakarta Sans (weights: 300, 400, 500, 600, 700, 800)
- **Why Plus Jakarta Sans?**: Modern, elegant, highly readable sans-serif with excellent character spacing. Popular in contemporary web design while maintaining professional academic aesthetic.
- **Alternative fonts to consider**: DM Sans, Outfit, Space Grotesk, Manrope
- **Title font size**: 4xl (mobile) → 5xl (tablet) → 6xl (desktop)
- **Body font size**: lg (18px) for abstract and main content

## File Structure

```
/
├── index.html          # Main landing page (single-file implementation)
├── paper.pdf          # Research paper PDF
└── claude.md          # This file - development notes and guidelines
```

## Design Decisions

### Single-File Architecture
- **Rationale**: Simplicity and ease of deployment
- All styles are inline or CDN-based
- No build process required
- Easy to maintain and update

### Responsive Breakpoints
- **Mobile**: Single column layout
- **Tablet** (md): 2 columns for results grid
- **Desktop** (lg): 4 columns for results grid

### Component Choices
- **Hero**: DaisyUI hero component with clean white background
- **Cards**: DaisyUI cards with simple shadows
- **Buttons**: DaisyUI outline buttons for minimal design
- **Code Block**: DaisyUI mockup-code for citation
- **Copy Button**: JavaScript-powered clipboard functionality with visual feedback

### Design Elements
- **Minimal styling**: Focus on content over decoration
- **Typography hierarchy**: Size and weight differences for visual structure
- **Subtle shadows**: Light drop shadows on cards
- **Clean spacing**: Generous whitespace for readability
- **Placeholder boxes**: Simple gray dashed borders

## Current Placeholders (TO UPDATE)

### 1. Author Links & Affiliations
**Location**: Hero section, author names and affiliations
**Current**:
- All author links point to `#`
- Affiliations show "Institution Name Placeholder"
- Superscript numbers: 1-4 for first four authors, 5 for last author
**Action needed**:
- Replace author links with actual profile URLs (personal websites, Google Scholar, etc.)
- Update affiliation text with actual institution names

```html
<!-- Example format -->
<a href="https://scholar.google.com/..." class="author-link">Joanna Kaleta<sup>1</sup></a>

<!-- Affiliations section -->
<div class="text-sm md:text-base mb-8 text-white/80">
    <p><sup>1</sup>Jagiellonian University</p>
    <p><sup>2</sup>Warsaw University of Technology</p>
</div>
```

### 2. Teaser Figure
**Location**: First section after hero
**Current**: Placeholder div with gradient background and icon
**Action needed**: Replace with actual teaser image

```html
<!-- Replace this div -->
<div class="placeholder-box h-[400px] md:h-[500px]">...</div>

<!-- With this -->
<figure class="mb-16">
    <img src="images/teaser.png" alt="AnyStyle teaser figure" class="rounded-lg shadow-xl w-full">
    <figcaption class="text-center mt-4 text-sm opacity-70">Figure caption here</figcaption>
</figure>
```

### 3. Animation/Results Placeholders
**Location**: Results section grid
**Current**: 4 placeholder divs
**Action needed**: Replace with actual videos, GIFs, or images

**Recommended formats:**
- MP4 videos with autoplay loop
- Animated GIFs
- Static comparison images

```html
<!-- Example video replacement -->
<div class="card bg-base-100 shadow-xl">
    <video autoplay loop muted playsinline class="w-full rounded-lg">
        <source src="videos/result1.mp4" type="video/mp4">
    </video>
    <div class="card-body p-4">
        <p class="text-sm text-center">Description of result</p>
    </div>
</div>
```

## Future Improvements

### High Priority
- [x] Add real teaser figure from paper (✅ `assets/teaser.jpg`)
- [x] Add result videos/animations (✅ Swiper carousel with split clips)
- [ ] Fill in author profile links (Bartosz Świrta still points to `#`)
- [ ] Add supplementary materials section (if available)
- [ ] Add project video (if created)

### Medium Priority
- [x] Add comparison section showing improvements over prior work (✅ `assets/comparison.jpg` in teaser)
- [ ] Add interactive demo or viewer (if applicable for 3D content)
- [x] Add "Method" section with architecture diagram (✅ `assets/method.jpg`)
- [ ] Add acknowledgments section
- [x] Implement copy-to-clipboard for BibTeX citation (✅ Completed)

### Low Priority / Nice-to-have
- [ ] Add dark mode toggle (DaisyUI supports this easily)
- [ ] Add animation on scroll effects
- [ ] Add meta tags for better social media sharing (Open Graph, Twitter Cards)
- [ ] Add Google Analytics or similar (if desired)
- [ ] Add related papers section
- [ ] Add news/updates section for paper acceptance, presentations, etc.

## Maintenance Guidelines

### Adding New Content
1. **Images**: Create an `images/` directory and reference relatively
2. **Videos**: Create a `videos/` directory or use external hosting (YouTube, etc.)
3. **Styles**: Add custom CSS in the `<style>` block in the `<head>`

### Updating Content
- **Abstract**: Modify text in the Abstract card body
- **Citation**: Update BibTeX in the mockup-code section
- **Links**: Update href attributes in buttons and author links
- **Author Affiliations**:
  - Update superscript numbers in `<sup>` tags next to author names
  - Update institution names in the affiliations div below authors
  - Adjust affiliation numbering if authors share institutions

### Performance Considerations
- Keep images optimized (WebP format preferred)
- Videos should be compressed (consider max 720p for web)
- Use lazy loading for images below the fold if page gets heavy

### Accessibility
- Always include alt text for images
- Ensure color contrast meets WCAG standards
- Test with screen readers if major changes are made
- Maintain semantic HTML structure

## DaisyUI Components Reference

### Used Components
- **Hero**: `.hero`, `.hero-content` - Main header section
- **Card**: `.card`, `.card-body` - Content containers
- **Button**: `.btn`, `.btn-lg` - Action buttons
- **Mockup Code**: `.mockup-code` - Citation block
- **Footer**: `.footer`, `.footer-center` - Page footer

### Useful Components Not Yet Used
- **Modal**: For larger images or video viewing
- **Carousel**: For showcasing multiple results
- **Tabs**: For organizing different result categories
- **Collapse**: For FAQ or additional details
- **Badge**: For highlighting key features or achievements

### Theme Customization
If you want to customize the DaisyUI theme, you can:
1. Switch themes by changing `data-theme` attribute on `<html>`
2. Available themes: light, dark, cupcake, bumblebee, emerald, corporate, etc.
3. Or create custom theme in Tailwind config (requires build process)

## Interactive Features

### Copy to Clipboard (Citation)
**Location**: Citation section, top-right button
**Functionality**:
- Copies BibTeX citation to clipboard using Navigator Clipboard API
- Button changes to "Copied!" with green success styling
- Automatically resets to original state after 2 seconds
- Error handling for browsers that don't support clipboard API

**Implementation**:
```javascript
function copyCitation() {
    const citation = document.getElementById('bibtex-citation').textContent;
    navigator.clipboard.writeText(citation).then(() => {
        // Success feedback with DaisyUI btn-success class
    }).catch(err => {
        // Error handling
    });
}
```

**Browser Compatibility**:
- Works on all modern browsers (Chrome, Firefox, Safari, Edge)
- Requires HTTPS in production (or localhost for development)
- Fallback error message if clipboard access is denied

## Common Tasks

### Modifying Hero Section
The hero section uses a simple white background. To modify:
```css
.hero-simple {
    background: #ffffff;
    color: #1a1a1a;
    border-bottom: 1px solid #e5e7eb;
}
```

### Adding a New Section
Follow this pattern:
```html
<section class="mb-16">
    <h2 class="text-3xl md:text-4xl font-bold mb-6 text-primary">Section Title</h2>
    <div class="card bg-base-100 shadow-xl">
        <div class="card-body">
            <!-- Content here -->
        </div>
    </div>
</section>
```

### Making Text Justify vs Left-Aligned
- Justified: `text-justify` (current for abstract)
- Left-aligned: `text-left`
- Centered: `text-center`

## Testing Checklist

Before deploying updates:
- [ ] Test on mobile (iPhone, Android)
- [ ] Test on tablet (iPad)
- [ ] Test on desktop (various screen sizes)
- [ ] Check all links work (PDF, arXiv, GitHub)
- [ ] Verify images load correctly
- [ ] Test video autoplay (may be blocked on some browsers)
- [ ] Test copy citation button (should show "Copied!" feedback)
- [ ] Check console for errors
- [ ] Test with slow network (to see loading behavior)
- [ ] Verify copy button works on HTTPS (required for clipboard API)

## GitHub Pages Deployment

This site is designed to be deployed on GitHub Pages at:
`https://anystyle3dgs.github.io`

**Setup:**
1. Push to `main` branch
2. Enable GitHub Pages in repository settings
3. Select source: `main` branch, root directory
4. Site will be live at the URL above

**Note**: Changes may take 1-2 minutes to appear after pushing.

## Browser Compatibility

Tested/expected to work on:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Android)

**Known Issues:**
- Video autoplay may be blocked on some mobile browsers (user must tap to play)
- Tailwind browser CDN is in beta (consider npm build for production if issues arise)

## Contact for Updates

If collaborators need to make updates:
1. Clone the repository
2. Edit `index.html` directly
3. Test locally (just open in browser)
4. Push changes to trigger GitHub Pages rebuild

**No build process needed** - this is intentional for ease of maintenance by non-technical users.

## Resources

- **DaisyUI Docs**: https://daisyui.com/
- **Tailwind CSS Docs**: https://tailwindcss.com/
- **Font Awesome Icons**: https://fontawesome.com/icons
- **Responsive Design Reference**: https://tailwindcss.com/docs/responsive-design

## Version History

- **v1.5** (2026-03-07): Icon and formatting fixes
  - Fixed GitHub icon floating issue by switching from `fab fa-github` to `fas fa-code`
  - Improved BibTeX citation formatting with aligned equals signs and proper indentation
  - Added CSS fix attempt for Font Awesome brand icons

- **v1.4** (2026-03-07): Simplified to truly minimal design
  - Removed all colorful gradients and accents
  - Switched to clean black, white, and gray palette
  - White hero background with subtle border
  - Outline buttons for minimal visual weight
  - Removed decorative elements (underlines, color accents)
  - Simple gray placeholders with dashed borders
  - Focus on typography and content over decoration

- **v1.3** (2026-03-07): Color scheme upgrade - Deep Blue & Cyan [REVERTED]
  - Completely redesigned color palette from purple/violet to deep blue & cyan
  - Three-color hero gradient (deep blue → teal → bright cyan)
  - Added CSS custom properties for consistent theming
  - Enhanced button hover effects with scale animation
  - Added cyan gradient underlines to section headings
  - Added cyan left border accent to all cards
  - Updated placeholder boxes to match blue theme
  - **Note**: This version was too colorful and reverted to minimal design in v1.4

- **v1.2** (2026-03-07): Interactive copy functionality
  - Added "Copy BibTeX" button to citation section
  - Implemented clipboard API with visual feedback (button turns green and shows "Copied!")
  - Auto-reset after 2 seconds
  - Error handling for clipboard failures

- **v1.1** (2026-03-07): Font upgrade and affiliation support
  - Changed font from Inter to Plus Jakarta Sans for more elegant typography
  - Added author affiliations with superscript numbering
  - Added placeholder affiliation institutions below author names
  - Updated abstract with full paper content
  - Updated citation year from 2025 to 2026

- **v1.0** (2026-03-07): Initial landing page creation
  - DaisyUI + Tailwind implementation
  - Hero, Abstract, Results placeholders, Citation sections
  - Responsive design

---

## Video Pipeline (`split_videos.py`)

> **Run with:** `uv run split_videos.py`  (plain `python3` will miss the venv dependencies)

### Purpose
Converts the raw supplementary videos into per-scene, per-row MP4 clips used by the Swiper carousel.

### Source material
Download **supplementary.zip** from the OpenReview submission and extract the three `.mp4` files to `supplementary/`:
- `01_Anystyle_re10k_image_vs_text.mp4`
- `02_Anystyle_re10k_natural_text_prompts.mp4`
- `03_Stylos_vs_Anystyle_comparison.mp4`

### Pipeline — two passes

**Pass 1 — Normalize to 25 fps**
- Re-encodes each source video to 25 fps using `ffmpeg` (H.264, CRF 17, preset slow).
- Output: `supplementary/normalized/<filename>.mp4`
- Updates `files.json` in-place with new paths and adds a `split_dir` key.
- If source is already in `normalized/` (idempotent re-run), re-encoding is skipped.

**Pass 2 — Split into carousel clips**
- `timestamps` in `files.json` are **frame numbers at 25 fps** (not seconds, not original fps).
- Segment 0 (frames 0 → `timestamps[0]−1`) is the **intro — discarded**.
- Remaining segments are each cropped vertically into `rows` equal-height sub-clips using ffmpeg `trim` + `crop` filters (frame-accurate, no keyframe approximation).
- Output: `supplementary/splits/<split_dir>/{0,1,2,...}.mp4` (segment-major, row-minor order).

### `files.json` schema
```json
{
  "filename": "./supplementary/normalized/<file>.mp4",  // updated by pass 1
  "timestamps": [100, 346, 560, 784],                   // frame numbers at 25 fps
  "rows": 3,                                            // vertical sub-clips per segment
  "split_dir": "stylos_vs_anystyle_comparison"          // output subdirectory name
}
```

### Carousel wiring
`index.html` reads `CAROUSELS` JS config (hardcoded) that maps each `split_dir` to a Swiper instance. Videos are built dynamically in JS — no hardcoded `<video>` tags.

---

## Static Assets

- `assets/teaser.jpg` — main teaser figure (provided)
- `assets/method.jpg` — architecture diagram (provided)
- `assets/comparison.jpg` — method comparison table, rasterised from `tex/comparison.pdf`:
  ```bash
  magick -density 400 tex/comparison.pdf -quality 95 assets/comparison.jpg
  ```

---

## Lighthouse Scores (as of v2.0)

| Category | Score |
|----------|-------|
| Accessibility | 96 |
| Best Practices | 100 |
| SEO | 100 |

Remaining advisory: Swiper pagination dots are slightly below the 24 px touch-target recommendation — acceptable visual tradeoff.

---

## Version History (continued)

- **v2.0** (2026-03-08): Video carousels, assets, and quality improvements
  - Added `split_videos.py` — two-pass ffmpeg pipeline (normalize + split)
  - Three Swiper.js carousels in Results section (image/text conditioning, natural prompts, Stylos comparison)
  - Nav arrows moved outside `overflow:hidden` with per-carousel IDs to prevent clipping
  - Method section with edge-to-edge architecture diagram
  - Teaser section: `assets/teaser.jpg` + `assets/comparison.jpg` side-by-side (40/60 split) with figcaptions
  - Added emoji favicon, meta description, `<main>` landmark
  - Lighthouse Best Practices 96→100, SEO 91→100, Accessibility 94→96
  - Added `README.md` with full reproduction instructions
  - Font Awesome icons
