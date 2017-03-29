import requests

url = "http://pulse-rest-testing.herokuapp.com/"
r = requests.get(url + "roles/")

user_list = r.json()

for user in user_list:
    print("Users: ", user["name"])

q = requests.get(url + "books/")
list_books =q.json()

for book in list_books:
    print("Books: ", book["title"])