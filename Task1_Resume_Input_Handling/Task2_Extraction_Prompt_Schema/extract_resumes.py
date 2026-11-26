import os
import fitz
from openai import OpenAI
import base64
import csv
import json
from pathlib import Path

import fitz
from openai import OpenAI

task_folder = Path(__file__).resolve().parent
resume_folder = task_folder.parent / "resumes"
prompt_file = task_folder / "prompts" / "extraction_prompt_v1.txt"
schema_file = task_folder / "schemas" / "resume_schema.json"
results_folder = task_folder / "results"

results_folder.mkdir(exist_ok=True)

system_prompt = prompt_file.read_text(encoding="utf-8")
schema = json.loads(schema_file.read_text(encoding="utf-8"))

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"]
)
model_name = "openai/gpt-oss-20b"


def read_resume_file(file_path):
    if file_path.suffix.lower() == ".txt":
        text = file_path.read_text(encoding="utf-8", errors="replace")
        return text, []

    if file_path.suffix.lower() == ".pdf":
        with fitz.open(file_path) as pdf:
            text = "\n".join(page.get_text() for page in pdf)

            if text.strip():
                return text, []

            images = []

            for page in pdf:
                pixmap = page.get_pixmap(dpi=120)
                image_bytes = pixmap.tobytes("png")
                image_base64 = base64.b64encode(image_bytes).decode("utf-8")

                images.append(
                    "data:image/png;base64," + image_base64
                )

            return "", images

    raise ValueError("Unsupported file type")


def extract_resume(file_path):
    resume_text, resume_images = read_resume_file(file_path)

    user_content = [
        {
            "type": "text",
            "text": (
                "Extract information from this resume.\n\n"
                "Use this JSON schema:\n"
                + json.dumps(schema, indent=2)
            )
        }
    ]

    if resume_text.strip():
        user_content.append(
            {
                "type": "text",
                "text": "Resume text:\n" + resume_text
            }
        )

    for image_data in resume_images:
        user_content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": image_data
                }
            }
        )

    response = client.chat.completions.create(
        model=model_name,
        temperature=0,
      response_format={
    "type": "json_schema",
    "json_schema": {
        "name": "resume_extraction",
        "strict": True,
        "schema": schema
    }
},
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_content
            }
        ]
    )

    response_text = response.choices[0].message.content
    extracted_data = json.loads(response_text)

    required_fields = [
        "candidate_name",
        "skills",
        "years_of_experience",
        "education",
        "strengths",
        "gaps"
    ]

    for field in required_fields:
        if field not in extracted_data:
            raise ValueError("Missing JSON field: " + field)

    return extracted_data


def main():
    resume_files = sorted(
        file_path
        for file_path in resume_folder.iterdir()
        if file_path.suffix.lower() in [".txt", ".pdf"]
    )

    print("Resume files found:", len(resume_files))

    summary_rows = []

    for file_path in resume_files:
        print("\nProcessing:", file_path.name)

        try:
            extracted_data = extract_resume(file_path)

            output_file = results_folder / (
                file_path.stem + "_extracted.json"
            )

            output_file.write_text(
                json.dumps(extracted_data, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )

            print("Saved:", output_file.name)

            summary_rows.append(
                {
                    "resume_file": file_path.name,
                    "status": "Success",
                    "error": ""
                }
            )

        except Exception as error:
            print("Error:", error)

            summary_rows.append(
                {
                    "resume_file": file_path.name,
                    "status": "Error",
                    "error": str(error)
                }
            )

    summary_file = results_folder / "extraction_summary.csv"

    with summary_file.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:
        fieldnames = ["resume_file", "status", "error"]

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(summary_rows)

    print("\nExtraction completed.")
    print("Summary saved to:", summary_file)


if __name__ == "__main__":
    main()
