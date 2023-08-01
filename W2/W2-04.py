
import requests

response = requests.get('https://www.google.com')

url = 'https://www.google.com'
print(response.status_code)
# 200#

response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
response = requests.get(url)

print(response.text[:50])
print(response.raise_for_status())