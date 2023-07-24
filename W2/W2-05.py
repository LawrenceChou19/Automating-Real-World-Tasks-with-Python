

#HTTPGET AND POST METHODS


p = {"search": "grey kitten","max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'

print(response.request.url)

p = {"description": "white kitten","name": "Snowball","age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
print(response.request.url)
print(response.request.body)

response = requests.post("https://example.com/path/to/api", json=p)
print(response.request.url)
'https://example.com/path/to/api'
print(response.request.body)
# b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 