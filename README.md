# Project Name
EPUB to Small Markdown Files Converter

## Project Description
A Python script to convert a single EPUB file into multiple Markdown files, breaking the text into chunks while preserving images/formulas and adhering to specific splitting rules.

## Target Audience
Users who want to segment lengthy EPUB content into smaller textual pieces without losing essential media like images/formulas.

## Desired Features

### Input
- [ ] Accept a single local EPUB file (no web interface).
- [ ] Extract the main text (including images, formulas).

### Output
- [ ] Produce multiple `.md` files, each representing a segment of the EPUB text.
- [ ] Preserve images (and formulas) so they remain accessible in the output.
  - [ ] Images can be extracted into a subfolder (e.g., `images/`) and referenced in the Markdown.

### Text Splitting Logic

1. **Paragraph-Level Processing**  
   - If a paragraph has **300 words or fewer**, keep it as a single chunk.  
   - If a paragraph has **between 301 and 400 words**, also keep it as a single chunk.  
   - If a paragraph has **more than 400 words**, split it at sentence boundaries so that each chunk is **at most 300 words**.  
     - **Exception**: If a single sentence is over 400 words by itself, keep that entire sentence in one chunk (even if it exceeds 400 words).

2. **Chunk Size Goals**  
   - Ideally, each chunk should have between **100 and 300 words**.  
   - Combine sentences within a paragraph up to 300 words; if adding another sentence would exceed 300, start a new chunk.  
   - If the last few sentences in a paragraph result in a smaller chunk under 100 words, that’s acceptable as long as we don’t exceed 300 in the previous chunk.

3. **Formatting**  
   - Only basic text is needed; no EPUB metadata (author, title, etc.).  
   - Preserve images/formulas in an accessible way (either inline or as separate files + Markdown references).  
   - No need for advanced Markdown formatting (bold, italics, lists), unless easily extracted from the EPUB.

### Performance & Constraints
- [ ] The script does not need advanced optimization; normal Python execution time is acceptable.
- [ ] Processing each file in a few seconds is fine.

## Design Requests
- [ ] Organize the output into a clear folder structure:
  - [ ] An `output/` folder containing sequentially named `.md` files (e.g., `part1.md`, `part2.md`, etc.).
  - [ ] A subfolder for extracted images (e.g., `output/images/`), referenced by the `.md` files.

## Other Notes
- The main challenge is to carefully split paragraphs over 400 words at sentence boundaries, aiming for 100–300 words per chunk.
- Large single sentences (> 400 words) remain un-split.
- This will be a simple, local Python script, not a hosted web service.
