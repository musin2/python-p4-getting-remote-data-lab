import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response_body = response.content
        return response_body

    def load_json(self):
        body_json = self.get_response_body()
        body_in_dict  = json.loads(body_json)
        return body_in_dict