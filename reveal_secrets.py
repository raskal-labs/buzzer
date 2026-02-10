import os
from twilio.rest import Client

# --- CONFIGURATION ---
ACCOUNT_SID = 'ACb4e45264b53b2292e1d0c787fb80b355'
AUTH_TOKEN = '545e4b945c4bb6dca9fbc7385f65cdca' # <--- PASTE YOUR TOKEN AGAIN
SERVICE_SID = 'ZSa7a008fd75c24c9e04d4da8f2f7a8205' 
ENV_SID = 'ZE412f1300e6d9aa3bc05fea20accb1d50'
# ---------------------

client = Client(ACCOUNT_SID, AUTH_TOKEN)

print(f"[-] Fetching secrets for Environment: {ENV_SID}...")

variables = client.serverless.v1.services(SERVICE_SID) \
    .environments(ENV_SID) \
    .variables.list(limit=100)

print("\n--- COPY BELOW THIS LINE ---\n")
print(f"ACCOUNT_SID={ACCOUNT_SID}")
print(f"AUTH_TOKEN={AUTH_TOKEN}")

for var in variables:
    # Some variables might be hidden, so we fetch the specific instance to be safe
    v_details = client.serverless.v1.services(SERVICE_SID) \
        .environments(ENV_SID) \
        .variables(var.sid).fetch()
    
    print(f"{v_details.key}={v_details.value}")

print("\n--- COPY ABOVE THIS LINE ---\n")
