from api_client import fetch_data
import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    config = load_config()

    try:
        data = fetch_data(config["api_url"], config["timeout"])
    except Exception as e:
        print("API request failed:", e)
        return

    for user in data:
        if "id" in user and "name" in user and "email" in user:
            print(f"ID: {user['id']} | Name: {user['name']} | Email: {user['email']}")
        else:
            print("Invalid user record:", user)

if __name__ == "__main__":
    main()


