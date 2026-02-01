# OpenClaw Issue Tracker 🐙

## Installation
```bash
git clone git@github.com:codi-opcl/issue-tracker.git
cd issue-tracker
chmod +x issue_tracker.py
```

## Usage
```
python3 issue_tracker.py add \"Cron bug\" --stakeholder Jake
python3 issue_tracker.py list
python3 issue_tracker.py status abc123
python3 issue_tracker.py close abc123
```

## Example Output
```
Added issue abc123: Cron bug
abc123 [OPEN] Cron bug - Jake
```

## JSON Format
```json
{
  \"id\": \"abc123\",
  \"title\": \"Cron bug\",
  \"status\": \"open\",
  \"history\": [
    {\"action\": \"opened\", \"timestamp\": \"2026-02-01T11:00:00\", \"by\": \"Jake\"}
  ],
  \"stakeholder\": \"Jake\"
}
```

## Status Values
- open
- pending
- in-progress
- awaiting-review
- approved
- closed