import requests
import time

def fetch_data(url, timeout, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(1)

