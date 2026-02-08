# Integration Support Toolkit (Python)

## What this does
A small Python tool that:
- Calls a public REST API
- Validates response data
- Handles API failures gracefully
- Produces structured, timestamped logs

## Why this exists
This project simulates real-world integration and support scenarios where:
- External APIs can fail
- Responses may be malformed
- Clear logs are required for investigation and escalation

## How to run
1. Install dependencies:
   pip install requests

2. Run:
   python scripts/main.py

## Skills demonstrated
- API consumption (REST, JSON)
- Defensive coding
- Error handling
- Logging
- Basic project structure

## Real-world relevance
This project simulates common integration scenarios faced by
Customer Success Engineers and Integration Support roles, including:
- API outages
- Invalid payloads
- Partial failures
- Customer impact analysis

## Investigation workflow
1. Run integration
2. Persist results
3. Query affected users
4. Escalate with evidence
