import requests

url = "http://dev.eddr-api-public.int10h.net"
r = requests.get(url + "/roles")
print(r.text)