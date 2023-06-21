import requests


headers = {'Authorization': 'Bearer 4ceea427aeea3540f384e14d459d664515c73141'}
endpoint = "http://localhost:8000/api/product/"

data = {
    "title": "this field is done",
    "price": 32.89
}

get_response = requests.post(endpoint, data, headers=headers)

print(get_response.json())


