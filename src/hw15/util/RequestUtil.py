import requests

from src.hw15.config.Data import BASE_URL


class RequestUtil:
    def __init__(self):
        self.status_code = None
        self.rs_json = None
        self.base_url = BASE_URL

    def get(self, endpoint, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.get(url=url, headers=headers)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), \
            f"Expected status code {expected_status_code}, but actual is {self.status_code}"
        self.rs_json = rs_api.json()
        return self.rs_json

    def delete(self, endpoint, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.delete(url=url, headers=headers)
        self.rs_json = rs_api.json()
        return self.rs_json


