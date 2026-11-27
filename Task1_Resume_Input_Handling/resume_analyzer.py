
import re
import csv
from pathlib import Path

import pymupdf
import tiktoken


def clean_text(text):
    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(
        r"(?im)^\s*(page\s*)?\d+\s*(of\s*\d+)?\s*$",
        "",
        text
    )

    text = re.sub(
        r"(?im)^\s*(resume|curriculum vitae)\s*$",
        "",
        text
    )

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" *\n *", "\n", text)

    return text.strip()


def read_resume(path):
    path = Path(path)

    if not path.exists():
        raise ValueError("File does not exist")

    if path.suffix.lower() == ".pdf":
        text = ""

        try:
            with pymupdf.open(path) as document:
                for page in document:
                    text += page.get_text() + "\n"
        except Exception:
            raise ValueError("Could not open PDF file")

        text = clean_text(text)

        if not text:
            raise ValueError(
                "no text found (scanned or empty PDF)"
            )

        return text

    elif path.suffix.lower() == ".txt":
        text = path.read_text(
            encoding="utf-8",
            errors="replace"
        )

        text = clean_text(text)

        if not text:
            raise ValueError("text file is empty")

        return text

    else:
        raise ValueError("Unsupported file format")


def count_tokens(text):
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)

    return len(tokens)


def analyze_resumes():
    resume_folder = Path("resumes")
    output_folder = Path("output")

    output_folder.mkdir(exist_ok=True)

    resume_files = []

    for file in resume_folder.iterdir():
        if file.suffix.lower() in [".pdf", ".txt"]:
            if not file.name.startswith("~$"):
                resume_files.append(file)

    resume_files = sorted(resume_files)

    if not resume_files:
        print("No resume files found.")
        return

    results = []

    for resume_path in resume_files:
        try:
            text = read_resume(resume_path)

            characters = len(text)
            tokens = count_tokens(text)

            print(
                f"{resume_path.name}: "
                f"{characters} characters, "
                f"{tokens} tokens"
            )

            results.append({
                "filename": resume_path.name,
                "characters": characters,
                "tokens": tokens,
                "status": "Success"
            })

        except Exception as error:
            print(
                f"{resume_path.name}: Error - {error}"
            )

            results.append({
                "filename": resume_path.name,
                "characters": 0,
                "tokens": 0,
                "status": f"Error - {error}"
            })

    report_path = output_folder / "resume_report.csv"

    with open(
        report_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "filename",
                "characters",
                "tokens",
                "status"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nReport saved to:", report_path)


if __name__ == "__main__":
    analyze_resumes()
