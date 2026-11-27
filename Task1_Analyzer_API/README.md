# Resume Analyzer API

## Purpose

The Resume Analyzer API analyzes resume text against a job description. It extracts relevant skills and provides structured results to help users review how well a resume matches a role.

The analyzer is an assistive tool. It should not be used as the sole basis for hiring decisions.

## Architecture

The application uses the following components:

- **FastAPI** — provides the API endpoint
- **LLM provider (Groq)** — processes resume and job description text
- **Pydantic** — validates structured data
- **pytest and TestClient** — test the API
- **coverage.py** — measures test coverage

Request flow:

1. User uploads resume text and a job description.
2. The API validates the input.
3. The resume and job description are sent to the language model.
4. The model returns structured analysis.
5. The API returns the result to the user.

## Setup

Create and activate the Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project directory and add your API key:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Never commit your real `.env` file or API key.

Create a `.env.example` file with this safe placeholder:

```text
GROQ_API_KEY=your_groq_api_key_here
```

## Run the API

Start the development server:

```powershell
python -m uvicorn api:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Example curl Request

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "job_description=Looking for Python and SQL skills" \
  -F "resume_text=Experienced developer with Python and SQL skills"
```

## Testing

Run the API tests:

```powershell
python -m pytest test_api.py -v
```

Run the coverage report:

```powershell
python -m coverage report -m
```

## Limitations

- The language model can miss skills or extract incorrect information.
- Results depend on the quality and completeness of the resume text.
- The model may produce inconsistent results across different runs.
- The analyzer does not verify whether resume claims are true.
- The score is an estimate and is not a guarantee of job performance.
- The API requires a valid provider API key and internet access.

## Fairness Note

Resume analysis can reflect biases present in training data or in the wording of the job description. The system should not infer protected characteristics or use them to rank candidates.

The results should be reviewed by a human. Hiring decisions should consider relevant qualifications, evidence, and context rather than relying only on an automated score.
