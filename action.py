import requests
import json


with open("key.txt") as f:
    key = f.read().strip()

with open("notes.txt", "r") as f:

    text = f.read()

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

headers = {"x-goog-api-key": key, "Content-Type": "application/json"}

prompt = 'extract action items from these notes. reply with only a json list, no extra words.each list looks like {"task": "...", "owner": "..."}. use "unknown" if there is no  owner. Notes:'+ text
body = {"contents":[{"parts": [{"text": prompt}]}]}


response = requests.post(url, headers=headers, json=body, timeout=60)

print(response.status_code)

data = response.json()



answer = data["candidates"][0]["content"]["parts"][0]["text"]

print(answer)

items = json.loads(answer)

for number , item in enumerate(items, 1):
    print(number, item["task"] ,"-", item["owner"])
