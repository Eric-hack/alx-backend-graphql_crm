from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import datetime

def log_crm_heartbeat():
    """Logs CRM heartbeat and optionally checks GraphQL responsiveness."""
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{now} CRM is alive\n"

    # Append heartbeat to file
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(log_message)

    # Optional: Query GraphQL 'hello' field to verify endpoint
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=False)

    try:
        query = gql("{ hello }")
        response = client.execute(query)
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"{now} GraphQL response: {response}\n")
    except Exception as e:
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"{now} GraphQL query failed: {e}\n")
