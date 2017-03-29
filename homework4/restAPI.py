import requests

url = "http://pulse-rest-testing.herokuapp.com/"

#roles
print("ROLES")
ps = requests.post(url + "roles/", data={"name": "Oksana Alekseienko", "type": "student", "level": "10", "book": "1"})
print("Post:", ps.url, "Status_code:", ps.status_code)

dict = ps.json()
id = dict["id"]

g = requests.get(url + "roles/" + str(id) + "/")
print("GET:", g.url, "Status_code:", g.status_code, "Info:", g.text)

p = requests.put(url + "roles/" + str(id) + "/", data={"type": "InfoPulse", "level": "3", "book": "2"})
print("Put:", p.url, "Status_code:", p.status_code, "Info:", p.text)

d = requests.delete(url + "roles/" + str(id) + "/")
print("Delete:", d.url, "Status_code:", d.status_code)


# books
print("BOOKS")

ps1 = requests.post(url + "books/", data={"title": "QA", "author": "Oksana Alekseienko"})
print("Post:", ps1.url, "Status_code:", ps1.status_code)

dict1 = ps1.json()
id1 = dict1["id"]

g1 = requests.get(url + "books/" + str(id1) + "/")
print("GET:", g1.url, "Status_code:", g1.status_code, "Info:", g1.text)

p1 = requests.put(url + "books/" + str(id1) + "/", data={"title": "SQL", "author": "Alekseienko"})
print("Put:", p1.url, "Status_code:", p1.status_code, "Info:", p1.text)

d1 = requests.delete(url + "books/" + str(id1) + "/")
print("Delete:", d1.url, "Status_code:", d1.status_code)