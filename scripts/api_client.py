import requests

def fetch_data(url, timeout):
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


