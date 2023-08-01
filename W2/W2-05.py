

#HTTPGET AND POST METHODS
import requests
import urllib.request as req
# https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15

p = {"search": "grey kitten","max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
response.request.url
print('response is',response)
print('response.request.url is',response.request.url)
#'https://example.com/path/to/api?search=grey+kitten&max_results=15'

p = {"description": "white kitten","name": "Snowball","age_months": 6}  
response = requests.post("https://example.com/path/to/api", data=p)
print('response = requests.post("https://example.com/path/to/api", data=p) is ',response.request.url)
#'https://example.com/path/to/api'
print('response.request.url is',response.request.url)
#response.request.url is https://example.com/path/to/api
print('response.request.body is',response.request.body)
#response.request.body is description=white+kitten&name=Snowball&age_months=6

response = requests.post("https://example.com/path/to/api", json=p)
print(response.request.url)
'https://example.com/path/to/api'

print(response.request.body)
# b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
# response = requests.post("https://ithelp.ithome.com.tw/search", data=p)
# response = requests.get("https://ithelp.ithome.com.tw/search", data=p)
response = req.Request("https://ithelp.ithome.com.tw/search",headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
with req.urlopen(response) as response:
    data = response.read().decode("utf-8")
print(data)
print('回應狀態：', response.status_code)
print('回應標頭：', response.headers['content-type'])
print('回應編碼：', response.encoding)
print('回應內容：', response.text[:100], '...')