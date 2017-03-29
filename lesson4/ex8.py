import requests

url = "http://pulse-rest-testing.herokuapp.com"
r = requests.get(url + "/roles")
print(r.text)

q = requests.get(url + "/roles" + "/1")
print(q.text)

w = requests.post(url + "/roles/", data={"name": "Oksana", "type": "student", "level": "10", "book": "1"})
print(w.status_code)

a = requests.put(url + "/roles/" + "25/", data={"level": "1010", "book": "2"})
print(a.status_code)

s = requests.delete(url + "/roles/" + "44/")
print(s.status_code)