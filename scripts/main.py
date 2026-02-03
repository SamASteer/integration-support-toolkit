import json
from api_client import fetch_data

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    data = fetch_data(config["api_url"], config["timeout"])
    print(data)

if __name__ == "__main__":
    main()

