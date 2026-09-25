#!/usr/bin/env python3
"""
Stable ReportLab renderer for Lisa morning-plan PDFs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)


FONT_PATH = Path("/Library/Fonts/Arial Unicode.ttf")
FONT_NAME = "ArialUnicodeTF"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", required=True)
    parser.add_argument("--meta", required=True)
    parser.add_argument("--date", required=False)
    return parser.parse_args()


def ensure_font() -> None:
    if not FONT_PATH.exists():
        raise FileNotFoundError(f"Required font missing: {FONT_PATH}")
    try:
        pdfmetrics.getFont(FONT_NAME)
    except KeyError:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT_PATH)))


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="LisaTitle",
            parent=styles["Title"],
            fontName=FONT_NAME,
            fontSize=21,
            leading=25,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#143d66"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LisaSubtitle",
            parent=styles["Normal"],
            fontName=FONT_NAME,
            fontSize=10.5,
            leading=13,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#3f6182"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LisaMeta",
            parent=styles["Normal"],
            fontName=FONT_NAME,
            fontSize=9,
            leading=11,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#69788a"),
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LisaH1",
            parent=styles["Heading1"],
            fontName=FONT_NAME,
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#143d66"),
            spaceBefore=8,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LisaH2",
            parent=styles["Heading2"],
            fontName=FONT_NAME,
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor("#1b5a92"),
            spaceBefore=7,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LisaH3",
            parent=styles["Heading3"],
            fontName=FONT_NAME,
            fontSize=10.5,
            leading=13,
            textColor=colors.HexColor("#31485f"),
            spaceBefore=6,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LisaBody",
            parent=styles["BodyText"],
            fontName=FONT_NAME,
            fontSize=9.5,
            leading=12.5,
            alignment=TA_LEFT,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LisaCode",
            parent=styles["Code"],
            fontName=FONT_NAME,
            fontSize=8.5,
            leading=11,
            backColor=colors.HexColor("#f3f6fa"),
            borderColor=colors.HexColor("#d7e1ea"),
            borderPadding=8,
            borderWidth=0.5,
            spaceAfter=8,
        )
    )
    return styles


def sanitize_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<font backcolor='#edf2f8'>\1</font>", escaped)
    return escaped


def flush_paragraph(buffer: list[str], story: list, styles) -> None:
    if not buffer:
        return
    text = " ".join(part.strip() for part in buffer if part.strip())
    if text:
        story.append(Paragraph(sanitize_inline(text), styles["LisaBody"]))
    buffer.clear()


def flush_list(items: list[str], story: list, styles) -> None:
    if not items:
        return
    story.append(
        ListFlowable(
            [
                ListItem(Paragraph(sanitize_inline(item), styles["LisaBody"]), leftIndent=8)
                for item in items
            ],
            bulletType="bullet",
            leftIndent=14,
        )
    )
    story.append(Spacer(1, 0.12 * cm))
    items.clear()


def markdown_to_story(markdown_text: str, styles) -> list:
    story = []
    paragraph_buffer: list[str] = []
    bullet_buffer: list[str] = []
    code_buffer: list[str] = []
    in_code = False

    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph(paragraph_buffer, story, styles)
            flush_list(bullet_buffer, story, styles)
            if in_code:
                story.append(Preformatted("\n".join(code_buffer), styles["LisaCode"]))
                code_buffer.clear()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_buffer.append(line)
            continue

        if not stripped:
            flush_paragraph(paragraph_buffer, story, styles)
            flush_list(bullet_buffer, story, styles)
            continue

        if stripped == "---":
            flush_paragraph(paragraph_buffer, story, styles)
            flush_list(bullet_buffer, story, styles)
            story.append(HRFlowable(width="100%", color=colors.HexColor("#d7e1ea"), thickness=0.8))
            story.append(Spacer(1, 0.12 * cm))
            continue

        if stripped.startswith("#"):
            flush_paragraph(paragraph_buffer, story, styles)
            flush_list(bullet_buffer, story, styles)
            level = len(stripped) - len(stripped.lstrip("#"))
            title = stripped[level:].strip()
            style_name = {1: "LisaH1", 2: "LisaH2"}.get(level, "LisaH3")
            story.append(Paragraph(sanitize_inline(title), styles[style_name]))
            continue

        bullet_match = re.match(r"^[-*]\s+(.+)$", stripped)
        ordered_match = re.match(r"^\d+\.\s+(.+)$", stripped)
        if bullet_match or ordered_match:
            flush_paragraph(paragraph_buffer, story, styles)
            bullet_buffer.append((bullet_match or ordered_match).group(1))
            continue

        if bullet_buffer:
            flush_list(bullet_buffer, story, styles)
        paragraph_buffer.append(stripped)

    if in_code and code_buffer:
        story.append(Preformatted("\n".join(code_buffer), styles["LisaCode"]))
    flush_paragraph(paragraph_buffer, story, styles)
    flush_list(bullet_buffer, story, styles)
    return story


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser()
    output_path = Path(args.output).expanduser()
    if not input_path.exists():
        raise FileNotFoundError(f"Input markdown not found: {input_path}")

    ensure_font()
    styles = build_styles()
    story = [
        Paragraph(sanitize_inline(args.title), styles["LisaTitle"]),
        Paragraph(sanitize_inline(args.subtitle), styles["LisaSubtitle"]),
        Paragraph(sanitize_inline(args.meta), styles["LisaMeta"]),
        HRFlowable(width="100%", color=colors.HexColor("#1b5a92"), thickness=1),
        Spacer(1, 0.25 * cm),
    ]
    story.extend(markdown_to_story(input_path.read_text(encoding="utf-8"), styles))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.6 * cm,
        title=args.title,
        author="Lisa",
        subject=f"Roman ranní plán {args.date or dt.date.today().isoformat()}",
    )
    doc.build(story)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
