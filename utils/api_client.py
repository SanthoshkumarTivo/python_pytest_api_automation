import requests
from utils.config import BASE_URL

class APIClient:

    @staticmethod
    def get(endpoint):
        return requests.get(f"{BASE_URL}{endpoint}")
    
    @staticmethod
    def post(endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}",json=payload)