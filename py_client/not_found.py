import requests


endpoint = "http://localhost:8000/api/product/1344565y65/"

get_response = requests.get(endpoint)

print(get_response.json())
print(get_response.text)



