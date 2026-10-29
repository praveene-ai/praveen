
# Task 2 - JSON, Environment Variables and Timeouts

import os
import json
import requests
from dotenv import load_dotenv



# Load environment variables from .env
load_dotenv()

# Read API key
API_KEY = os.getenv("API_KEY")

print("REST API Task 2 Started")

if not API_KEY:
    raise ValueError("API_KEY not found. Check your .env file.")





# Read API key
API_KEY = os.getenv("API_KEY")

print("REST API Task 2 Started")

if not API_KEY:
    raise ValueError("API_KEY not found. Check your .env file.")

print("API key loaded successfully")


print("API key loaded successfully")

# 1. Call /headers with X-API-Key
headers = {
    "X-API-Key": API_KEY
}

try:
    response = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5
    )
    response.raise_for_status()
    data = response.json()

    received_headers = data.get("headers", {})
    received_key = received_headers.get("X-Api-Key", "Not shown")

    print(f"Server received key: {received_key}")

except requests.exceptions.RequestException as e:
    print(f"Headers request failed: {e}")


# 2. Demonstrate a timeout
try:
    response = requests.get(
        "https://httpbin.org/delay/5",
        timeout=3
    )
    response.raise_for_status()

    print("Delay request completed")

except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")

except requests.exceptions.RequestException as e:
    print(f"Delay request failed: {e}")



# 3. Handle HTTP 500 server error
try:
    response = requests.get(
        "https://httpbin.org/status/500",
        timeout=5
    )
    response.raise_for_status()

    print("Server request successful")

except requests.exceptions.HTTPError:
    print("Server error 500 handled")

except requests.exceptions.RequestException as e:
    print(f"Server request failed: {e}")


# 4. Parse nested JSON
sample_json = """
{
    "user": {
        "name": "Demo User",
        "details": {
            "city": "Chennai",
            "skills": ["Python", "JSON", "REST API"]
        }
    }
}
"""

data = json.loads(sample_json)

name = data["user"]["name"]
city = data["user"]["details"]["city"]
skills = data["user"]["details"]["skills"]

print("Nested JSON parsed successfully")
print("Name:", name)
print("City:", city)
print("Skills:", skills)



# 5. Save results to result.json
result = {
    "user": name,
    "city": city,
    "skills": skills,
    "api_key_loaded": True
}

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)

print("Result saved to result.json")
print("REST API Task 2 Completed")

