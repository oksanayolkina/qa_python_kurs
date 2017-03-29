import requests

url = "http://pulse-rest-testing.herokuapp.com/"

w = requests.post(url + "roles/", data={"name": "Oksana", "type": "student", "level": "10", "book": "1"})
print(w.status_code)

dict = w.json()
id = dict["id"]

r = requests.delete(url + "roles/" + str(id) + "/")
print(r.url)
print(r.status_code)