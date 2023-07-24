>>> response.status_code
200

response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

response = requests.get(url)
response.raise_for_status()