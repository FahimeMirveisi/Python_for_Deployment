import requests

url = "https://api.monsterapi.ai/v1/generate/txt2img"

payload = {
    "safe_filter": True,
    "prompt": "A vase of bright 6 red carnations on the table next to a book and a cup of coffee. Natural light shines through the window and shines on the carnation petals.",
    "negprompt": "deformed, worst quality, poor details, "
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjlkMjBmZGZjMzZmNzBlYjdiYjc2Yzk1NDgyY2QwOWY4IiwiY3JlYXRlZF9hdCI6IjIwMjQtMTEtMDVUMjE6MDI6NDkuMjM4MTMxIn0.s2-a2L6hnWiQVJQnSkvut-evDTAsZbJp2nSpFEjQfEg"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)