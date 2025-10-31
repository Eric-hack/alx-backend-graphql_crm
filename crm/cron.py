import datetime
import requests

def log_crm_heartbeat():
    """Logs CRM heartbeat and checks GraphQL endpoint responsiveness."""
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{now} CRM is alive\n"

    # Append to heartbeat log
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(log_message)

    # Optional: Check if GraphQL endpoint responds
    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            if response.status_code == 200:
                f.write(f"{now} GraphQL endpoint responsive\n")
            else:
                f.write(f"{now} GraphQL check failed (Status: {response.status_code})\n")
    except Exception as e:
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"{now} Error checking GraphQL endpoint: {e}\n")
