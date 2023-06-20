import requests


endpoint = "http://localhost:8000/api/product/"

data = {
    "title": "this field is done",
    "price": 32.89
}

get_response = requests.post(endpoint, data)

print(get_response.json())


