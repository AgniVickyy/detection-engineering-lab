# Detection Engineering Framework

A Python-based detection engineering project that analyzes Windows event logs, applies rule-based detections, maps findings to MITRE ATT&CK techniques, and generates investigation reports.

## Features

- Rule-based detection engine
- Windows event log analysis
- MITRE ATT&CK mapping
- Automated report generation
- Extensible JSON detection rules
- Interactive dashboard support

## Project Structure

```text
detection-engineering-framework/

├── rules/
├── logs/
├── reports/
├── detection_engine.py
├── report_generator.py
├── dashboard.py
├── requirements.txt
└── README.md
```

## Example Detections

| Detection | MITRE ATT&CK |
|------------|-------------|
| Encoded PowerShell | T1059.001 |
| Brute Force Login | T1110 |
| Credential Dumping | T1003 |
| Admin Account Creation | T1136 |

## Technologies

- Python
- JSON
- Streamlit
- MITRE ATT&CK

## Skills Demonstrated

- Detection Engineering
- Threat Detection
- Security Automation
- Log Analysis
- SOC Operations
- Python Development

## Future Enhancements

- Sigma rule conversion
- IOC matching
- Sysmon support
- HTML reporting
- Threat hunting integration
