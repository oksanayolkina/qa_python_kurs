import requests

url = "http://httpbin.org/get"

h = {"user-agent": "my-app/0.0.1"}
r = requests.get(url, headers=h)

print(r.text)


payload = {"key1": "value1", "key2": "value2"}
r = requests.get(url, params=payload)
print(r.url)
