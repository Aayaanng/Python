"""
Resume Analyzer powered by Google Gemini
==========================================

Compares a resume against a job description and returns a structured
analysis: match score, matched/missing skills, strengths, gaps, and
suggestions for improvement.

Setup:
    pip install google-genai PyPDF2 python-docx
    export GEMINI_API_KEY="your-api-key-here"

Usage:
    python resume_analyzer.py --resume resume.pdf --job job_description.txt
    python resume_analyzer.py --resume resume.docx --job "Paste JD text directly"
"""

import argparse
import json
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types

import PyPDF2
import docx


MODEL_NAME = "gemini-3.5-flash"  # fast + cheap; swap to gemini-2.5-pro for deeper analysis


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------

def extract_text_from_pdf(path: Path) -> str:
    text_parts = []
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    return "\n".join(text_parts)


def extract_text_from_docx(path: Path) -> str:
    document = docx.Document(str(path))
    return "\n".join(p.text for p in document.paragraphs if p.text.strip())


def extract_text_from_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_resume_text(resume_path: str) -> str:
    """Load resume content from a PDF, DOCX, or TXT file."""
    path = Path(resume_path)
    if not path.exists():
        raise FileNotFoundError(f"Resume file not found: {resume_path}")

    suffix = path.suffix.lower()
    if suffix == ".pdf":
        text = extract_text_from_pdf(path)
    elif suffix == ".docx":
        text = extract_text_from_docx(path)
    elif suffix == ".txt":
        text = extract_text_from_txt(path)
    else:
        raise ValueError(f"Unsupported resume format: {suffix} (use .pdf, .docx, or .txt)")

    if not text.strip():
        raise ValueError("No text could be extracted from the resume file. "
                          "It may be a scanned/image-based PDF.")
    return text.strip()


def load_job_description(job_arg: str) -> str:
    """Accept either a path to a file, or raw job description text."""
    path = Path(job_arg)
    if path.exists() and path.is_file():
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            return extract_text_from_pdf(path).strip()
        elif suffix == ".docx":
            return extract_text_from_docx(path).strip()
        else:
            return extract_text_from_txt(path).strip()
    # Not a file path -> treat the argument itself as the JD text
    return job_arg.strip()


# ---------------------------------------------------------------------------
# Gemini analysis
# ---------------------------------------------------------------------------

ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "match_score": {
            "type": "integer",
            "description": "Overall fit score from 0-100"
        },
        "summary": {
            "type": "string",
            "description": "2-3 sentence overall assessment"
        },
        "matched_skills": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Skills/requirements from the JD that the resume clearly covers"
        },
        "missing_skills": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Skills/requirements from the JD not evidenced in the resume"
        },
        "strengths": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Notable strengths of the resume relative to this role"
        },
        "gaps": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Weaknesses, gaps, or red flags relative to this role"
        },
        "improvement_suggestions": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Concrete, actionable edits to improve the resume for this job"
        },
        "ats_keywords_to_add": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Specific keywords/phrases worth adding for ATS keyword matching"
        }
    },
    "required": [
        "match_score", "summary", "matched_skills", "missing_skills",
        "strengths", "gaps", "improvement_suggestions", "ats_keywords_to_add"
    ]
}


def build_prompt(resume_text: str, job_text: str) -> str:
    return f"""You are an expert technical recruiter and resume coach with deep experience in
applicant tracking systems (ATS) and hiring across tech, business, and operations roles.

Analyze the RESUME against the JOB DESCRIPTION below. Be honest and specific — do not
inflate the match score. Base every claim strictly on what is actually written in the
resume; do not assume skills that aren't stated or strongly implied.

=== JOB DESCRIPTION ===
{job_text}

=== RESUME ===
{resume_text}

Return your analysis as JSON matching the required schema. Guidelines:
- match_score: 0-100, where 100 means the resume is an ideal match for every requirement.
  Be realistic; a typical decent-but-imperfect match should land in the 50-75 range.
- matched_skills / missing_skills: pull these directly from requirements implied or stated
  in the job description.
- improvement_suggestions: should be concrete rewrites or additions, not generic advice
  like "tailor your resume" — say exactly what to change.
- ats_keywords_to_add: exact phrases from the job description that are missing from the
  resume verbatim and would help with keyword-matching ATS systems.
"""


def analyze_resume(resume_text: str, job_text: str, api_key: str | None = None) -> dict:
    """Send resume + job description to Gemini and return structured analysis."""
    client = genai.Client(api_key=api_key) if api_key else genai.Client()

    prompt = build_prompt(resume_text, job_text)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ANALYSIS_SCHEMA,
            temperature=0.3,
        ),
    )

    return json.loads(response.text)


# ---------------------------------------------------------------------------
# Pretty printing
# ---------------------------------------------------------------------------

def print_report(analysis: dict) -> None:
    score = analysis["match_score"]
    bar_len = 30
    filled = round(bar_len * score / 100)
    bar = "█" * filled + "░" * (bar_len - filled)

    print("\n" + "=" * 60)
    print("  RESUME MATCH REPORT")
    print("=" * 60)
    print(f"\n  Match Score: {score}/100")
    print(f"  [{bar}]\n")
    print(f"  Summary: {analysis['summary']}\n")

    def section(title, items, bullet="✓"):
        print(f"  {title}")
        if items:
            for item in items:
                print(f"    {bullet} {item}")
        else:
            print("    (none)")
        print()

    section("MATCHED SKILLS", analysis["matched_skills"], "✓")
    section("MISSING SKILLS", analysis["missing_skills"], "✗")
    section("STRENGTHS", analysis["strengths"], "+")
    section("GAPS / WEAKNESSES", analysis["gaps"], "-")
    section("IMPROVEMENT SUGGESTIONS", analysis["improvement_suggestions"], "→")
    section("ATS KEYWORDS TO ADD", analysis["ats_keywords_to_add"], "#")
    print("=" * 60 + "\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analyze a resume against a job description using Google Gemini."
    )
    parser.add_argument("--resume", required=True, help="Path to resume file (.pdf, .docx, .txt)")
    parser.add_argument("--job", required=True, help="Path to job description file, or raw JD text")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of a formatted report")
    parser.add_argument("--out", help="Optional path to save the JSON result")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: Set the GEMINI_API_KEY environment variable first.\n"
              "  export GEMINI_API_KEY='AQ.Ab8RN6JtIDlz4V_VtIcNGhxCPWNOGaXQ2CbhJhzRFQfNLp-hmQ'", file=sys.stderr)
        sys.exit(1)

    try:
        resume_text = load_resume_text(args.resume)
        job_text = load_job_description(args.job)
    except (FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    print("Analyzing resume against job description...", file=sys.stderr)

    try:
        analysis = analyze_resume(resume_text, job_text, api_key=api_key)
    except Exception as e:
        print(f"ERROR: Gemini API call failed: {e}", file=sys.stderr)
        sys.exit(1)

    if args.out:
        Path(args.out).write_text(json.dumps(analysis, indent=2))
        print(f"Saved JSON result to {args.out}", file=sys.stderr)

    if args.json:
        print(json.dumps(analysis, indent=2))
    else:
        print_report(analysis)


if __name__ == "__main__":
    main()