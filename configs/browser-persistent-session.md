# Browser Persistent Session Setup

## Configuration for Lisa — Web Audit Browser

### Session Initialization
```bash
openclaw browser action=open url=https://jablickar.cz label=jablickar-audit
```

**Returns:**
- `targetId`: stable reference for all future calls
- `suggestedTargetId`: use this in subsequent actions
- `tabId`: fallback identifier

### Persistent Tab Management

#### Tab 1: Jablickar Audit
```json
{
  "label": "jablickar-audit",
  "url": "https://jablickar.cz",
  "purpose": "Content audit, byline inspection, schema validation",
  "actions": ["navigate", "screenshot", "evaluate"]
}
```

#### Tab 2: Competitors
```json
{
  "label": "competitor-audit",
  "url": "https://letemsvetemapplem.eu",
  "purpose": "Competitive intelligence, content structure comparison",
  "actions": ["navigate", "screenshot", "evaluate"]
}
```

#### Tab 3: Developer Tools
```json
{
  "label": "dev-inspection",
  "url": "about:blank",
  "purpose": "Ad-hoc web inspection, network debugging",
  "actions": ["evaluate", "screenshot"]
}
```

### Workflow Pattern

**1. Navigate to article:**
```bash
browser action=navigate targetId=jablickar-audit url=[ARTICLE_URL]
```

**2. Screenshot:**
```bash
browser action=screenshot targetId=jablickar-audit labels=true
```

**3. Extract metadata:**
```bash
browser action=act targetId=jablickar-audit kind=evaluate fn=[JS_FUNCTION]
```

**4. Log findings:**
```json
{
  "url": "[ARTICLE_URL]",
  "screenshot": "[PATH]",
  "byline": "[AUTHOR]",
  "featured_image": "[YES/NO]",
  "word_count": "[NUMBER]",
  "schema_markup": "[TYPES]"
}
```

### Performance Notes
- **Screenshot time:** 2–3 sec per article
- **Evaluate time:** 1–2 sec (JavaScript execution)
- **Network latency:** 1–2 sec (page load)
- **Total per article:** ~5–7 seconds

### Reusable Tab Pattern
```bash
# Check if tab exists
openclaw browser action=tabs

# If not found, create:
openclaw browser action=open url=[URL] label=[LABEL]

# Reuse existing:
openclaw browser action=navigate targetId=[LABEL] url=[NEW_URL]
```

### Memory Management
- Close unused tabs: `browser action=close targetId=[LABEL]`
- Keep max 3 tabs open (memory efficient)
- Refresh tab if stale: `browser action=navigate targetId=[LABEL] url=[SAME_URL]`

### Browser Profile
- **Profile:** Default (isolated, no login needed)
- **Timeout:** 30000ms for snapshots
- **Headless:** false (visual feedback useful for debugging)

### Error Recovery
```
If snapshot timeout:
  1. Check browser status: openclaw browser action=status
  2. Retry with longer timeout
  3. Close tab and reopen

If evaluate fails:
  1. Screenshot first (visual state check)
  2. Verify element selectors in DOM
  3. Retry evaluation
```

## Usage Example — Lisa's Daily Audit

```bash
# Initialize
browser action=open url=https://jablickar.cz label=jablickar-audit

# Audit loop (3 articles)
for article_url in [list]:
    browser action=navigate targetId=jablickar-audit url=$article_url
    browser action=screenshot targetId=jablickar-audit
    browser action=act targetId=jablickar-audit kind=evaluate fn=extract_metadata()
    # log findings
    
# Close session
browser action=close targetId=jablickar-audit
```

## Integration with Audit Skill
This persistent session serves as the foundation for the `web-article-analyzer` skill:
- Tab lifecycle management
- Efficient article navigation
- Screenshot collection
- Metadata extraction pipeline

## Future: Headless Chrome PDF
```bash
# Instead of WeasyPrint, use Chrome headless for faster PDF:
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --print-to-pdf=output.pdf \
  --print-to-pdf-no-header \
  --no-margins \
  "file:///path/to/report.html"
```
