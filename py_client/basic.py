import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"title": "abe123", "content": "hello world", "price": "asqw3"})
# print(get_response.status_code)
print(get_response.json())
# print(get_response.text)

