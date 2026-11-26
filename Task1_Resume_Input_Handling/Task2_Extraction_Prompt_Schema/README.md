# Task 2 – Extraction Prompt and Schema

## Objective
Extract structured information from resumes using an extraction prompt and JSON schema.

## JSON Schema
The extraction schema contains the following fields:

- `candidate_name`: Candidate's name or null
- `skills`: List of skills
- `years_of_experience`: Total years of experience or null
- `education`: List of education details
- `strengths`: List of strengths supported by resume evidence
- `gaps`: List of missing or unclear information

## System Prompt
The system prompt defines the role, task, output format, and constraints.

The model is instructed to:
- Extract information accurately from the resume
- Return valid JSON matching the schema
- Never invent or guess information
- Use null when a value is missing
- Use empty lists when no list information is available
- Identify gaps only when information is missing or unclear

## Model and Settings
- Provider: Groq API
- Model: `openai/gpt-oss-20b`
- Temperature: 0
- Output format: JSON

## Extraction Results
- Total resumes: 8
- Successfully extracted: 7
- Failed: 1
- Success rate: 87.5%

The scanned PDF could not be extracted because it contains image-based text and requires OCR.

## Manual Verification
Three successfully extracted resumes were selected for manual verification.

The extracted JSON files were compared with the original resumes to check candidate name, skills, experience, education, strengths, and gaps.

Manual verification error count: **[Enter your verified error count]**

## Conclusion
The extraction prompt and schema successfully extracted structured information from 7 out of 8 resumes. The scanned PDF requires OCR before extraction can be completed.
