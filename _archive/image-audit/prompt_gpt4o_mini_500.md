# Image SEO Audit Prompt - GPT-4o-mini

Use this prompt for the local batch controller that processes the AndroidMagazine media library in chunks of 500.

## Goal

For each image, generate SEO-ready metadata that is useful, accurate, and written in Czech.

## Input

- WordPress media items from `https://androidmagazine.eu/wp-json/wp/v2/media`
- Order: oldest first
- Image types only: JPEG, PNG, WEBP, GIF
- Existing `alt_text` must be reviewed, not blindly overwritten

## Required Output

Return a single JSON object with these fields:

- `alt_text`: short Czech description of what is visible in the image
- `title`: short SEO-friendly title in Czech
- `confidence`: integer `1` to `5`
- `action`: one of `UPDATE`, `KEEP`, `MANUAL_REVIEW`
- `reason`: short Czech explanation of the choice

## Rules

- Describe only what is visible in the image.
- Do not invent a device model if it is not clearly visible.
- Prefer precise, concrete descriptions over generic ones.
- Keep `alt_text` natural and readable.
- Keep `title` short and useful for SEO.
- Preserve any clearly supported model, variant, or color from the original title or filename when it is safe to do so.
- If the image clearly shows a variant already hinted by the source name, keep that detail in `title` instead of collapsing it to a generic device name.
- Do not drop meaningful identifiers like `Note 3`, `S5`, `Gold`, `Black`, `White`, or `Neo` when they are supported by the source data.
- If the image is unclear, generic, or low-signal, lower confidence and choose `MANUAL_REVIEW`.
- If the existing `alt_text` is already strong, choose `KEEP`.
- If the existing `alt_text` is weak, empty, or generic, choose `UPDATE`.
- Do not output anything except valid JSON.

## Quality bar

- Good: identifies visible device, object, UI, or scene with useful specificity.
- Bad: generic phrases like `smartphone`, `obrázek`, `snímek obrazovky`, or hallucinated model names.
- If uncertain, say so through `confidence` and `action`, not by guessing.
