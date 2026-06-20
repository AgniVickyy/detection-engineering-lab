import json
import os

RULE_DIR = "rules"
LOG_FILE = "logs/windows_events.json"

rules = []

for file in os.listdir(RULE_DIR):

    if file.endswith(".json"):

        with open(os.path.join(RULE_DIR, file)) as f:
            rules.append(json.load(f))

with open(LOG_FILE) as f:
    events = json.load(f)

alerts = []

for event in events:

    for rule in rules:

        if event.get("event_id") != rule.get("event_id"):
            continue

        keyword = rule.get("keyword")

        if keyword:

            command = event.get("command", "").lower()

            if keyword.lower() not in command:
                continue

        alerts.append({
            "name": rule["name"],
            "severity": rule["severity"],
            "mitre": rule["mitre"],
            "event": event
        })

print("\n=== Detection Results ===\n")

for alert in alerts:

    print(f"[{alert['severity']}]")
    print(alert["name"])
    print(alert["mitre"])
    print()