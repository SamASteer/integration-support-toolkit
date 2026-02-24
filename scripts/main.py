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
    init_db() #
    from db import save_result
    
    try:
        data = fetch_data(config["api_url"], config["timeout"])
    except Exception as e:
        log("error", f"CRITICAL: Integration failed to start: {e}")
        return

# Process records
    for user in data:
        required_fields = ["id", "name", "email"]
        missing = [field for field in required_fields if field not in user]

        if not missing:
            save_result(user['id'], user['name'], user['email'], "success")
            log("info", f"Stored user {user['id']}")
        else:
            save_result(None, None, None, "invalid_data")
            log("error", f"Malformed user record: missing {', '.join(missing)}")

    # Final Polish: The Stakeholder Summary
    print("\n" + "="*30)
    log("info", "RUN COMPLETE - GENERATING SUMMARY")
    
    # Get the specific failures
    from queries import get_invalid_user_ids
    invalid_ids = get_invalid_user_ids()
    
    if invalid_ids:
        log("warn", f"The following User IDs failed validation: {invalid_ids}")
    else:
        log("info", "All records processed successfully!")



if __name__ == "__main__":
    main()


