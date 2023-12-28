import requests

# base_url = 'http://127.0.0.1:5000/uppercase?text=hello world 123'

base_url = 'https://book-review-api-yuah.onrender.com/upper'

params = {'text': 'hello world'}

response = requests.get(base_url, params=params)

# response = requests.get(base_url)

print(response.json())