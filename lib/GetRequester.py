import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass
        URL = " https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(URL)
        return response.content

    def load_json(self):
        pass
        people_lists = []
        people = json.load(self.get_response_body())
        for person in people:
            people_lists.append(person["name"])
        return people_lists
    
people = GetRequester()

people_names = people.load_json()

for name in set(people_names):
    print(name)
