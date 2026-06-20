import json
import os

RULE_DIR = "rules"
LOG_FILE = "logs/windows_events.json"
REPORT = "reports/report.html"

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

            if keyword.lower() not in event.get(
                "command", ""
            ).lower():
                continue

        alerts.append(rule)

html = """
<html>
<head>
<title>Detection Report</title>
</head>
<body>

<h1>Detection Engineering Report</h1>

<table border="1">
<tr>
<th>Rule</th>
<th>Severity</th>
<th>MITRE</th>
</tr>
"""

for alert in alerts:

    html += f"""
    <tr>
    <td>{alert['name']}</td>
    <td>{alert['severity']}</td>
    <td>{alert['mitre']}</td>
    </tr>
    """

html += """
</table>
</body>
</html>
"""

with open(REPORT, "w") as f:
    f.write(html)

print("HTML report generated.")