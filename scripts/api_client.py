import requests
import time
from logger import log

def fetch_data(url, timeout, retries=3, delay=2):
    """
    Fetches data with a retry mechanism to handle transient network issues.
    """
    for i in range(retries):
        try:
            log("info", f"Attempt {i+1} to fetch data...")
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if i < retries - 1:
                log("warn", f"Attempt {i+1} failed. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                log("error", f"All {retries} attempts failed.")
                raise e
