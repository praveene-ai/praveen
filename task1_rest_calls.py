# task 1 

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("REST API Task Started")


# GET /users
response = requests.get(BASE_URL + "/users")

users = response.json()

for user in users[:5]:
    print(user["id"], "-", user["name"], "-", user["email"])


import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("REST API Task Started")

# GET /users
response = requests.get(BASE_URL + "/users")

users = response.json()

for user in users[:5]:
    print(user["id"], "-", user["name"], "-", user["email"])    


# POST /posts
post_data = {
    "title": "My First REST API Post",
    "body": "Learning REST API with Python",
    "userId": 1
}

response = requests.post(BASE_URL + "/posts", json=post_data)

print("POST:", response.status_code, ", id:", response.json()["id"])



import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("REST API Task Started")

# GET /users
response = requests.get(BASE_URL + "/users")

users = response.json()

for user in users[:5]:
    print(user["id"], "-", user["name"], "-", user["email"])


# POST /posts
post_data = {
    "title": "My First REST API Post",
    "body": "Learning REST API with Python",
    "userId": 1
}

response = requests.post(BASE_URL + "/posts", json=post_data)

print("POST:", response.status_code, ", id:", response.json()["id"])



# PUT /posts/1
put_data = {
    "id": 1,
    "title": "Updated Post",
    "body": "This post was updated",
    "userId": 1
}

put_response = requests.put(BASE_URL + "/posts/1", json=put_data)


# PATCH /posts/1
patch_data = {
    "title": "Partially Updated Post"
}

patch_response = requests.patch(BASE_URL + "/posts/1", json=patch_data)


# DELETE /posts/1
delete_response = requests.delete(BASE_URL + "/posts/1")


print(
    "PUT:", put_response.status_code,
    "| PATCH:", patch_response.status_code,
    "| DELETE:", delete_response.status_code
)


import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("REST API Task Started")

# GET /users
response = requests.get(BASE_URL + "/users")

users = response.json()

for user in users[:5]:
    print(user["id"], "-", user["name"], "-", user["email"])


# POST /posts
post_data = {
    "title": "My First REST API Post",
    "body": "Learning REST API with Python",
    "userId": 1
}

response = requests.post(BASE_URL + "/posts", json=post_data)

print("POST:", response.status_code, ", id:", response.json()["id"])


# PUT /posts/1
put_data = {
    "id": 1,
    "title": "Updated Post",
    "body": "This post was updated",
    "userId": 1
}

put_response = requests.put(BASE_URL + "/posts/1", json=put_data)


# PATCH /posts/1
patch_data = {
    "title": "Partially Updated Post"
}

patch_response = requests.patch(BASE_URL + "/posts/1", json=patch_data)


# DELETE /posts/1
delete_response = requests.delete(BASE_URL + "/posts/1")


print(
    "PUT:", put_response.status_code,
    "| PATCH:", patch_response.status_code,
    "| DELETE:", delete_response.status_code
)


# GET /posts/9999
not_found_response = requests.get(BASE_URL + "/posts/9999")

print("GET /posts/9999 ->", not_found_response.status_code)

if not_found_response.status_code == 404:
    print("Not found")


print(
    "PUT:", put_response.status_code,
    "| PATCH:", patch_response.status_code,
    "| DELETE:", delete_response.status_code
)


# GET /posts/9999
not_found_response = requests.get(BASE_URL + "/posts/9999")

print("GET /posts/9999 ->", not_found_response.status_code)

if not_found_response.status_code == 404:
    print("Not found")    


# Explain HTTP status codes
def explain_status(code):
    messages = {
        200: "OK - Request successful",
        201: "Created - New resource created",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error"
    }

    return messages.get(code, "Unknown status code")


print(explain_status(200))
print(explain_status(201))
print(explain_status(400))
print(explain_status(401))
print(explain_status(404))
print(explain_status(500))    