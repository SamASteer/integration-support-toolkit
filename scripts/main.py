from db import init_db
from logger import log
from api_client import fetch_data
from queries import count_by_status
import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    config = load_config()
    init_db()
    from db import save_result
    if config.get("simulate_failure"):
        raise Exception("Simulated API failure")

    try:
        data = fetch_data(config["api_url"], config["timeout"])
    except Exception as e:
        log("error", f"API request failed: {e}")
        return

    for user in data:
        if "id" in user and "name" in user and "email" in user:
            save_result(user["id"], user["name"], user["email"], "success")
            log("info", f"Stored user {user['id']}")
        else:
            save_result(None, None, None, "invalid")
            log("error", "Invalid user record")



if __name__ == "__main__":
    main()


