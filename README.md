# 🛡️ ScamShield AI — Multi-Agent Scam & Fraud Detection Assistant

## 📌 Problem Statement
Scam and fraud messages — phishing texts, fake lottery notifications, investment scams, impersonation attempts — are becoming increasingly sophisticated and hard for the average person to spot. Most people don't have the domain knowledge to judge whether a suspicious message is safe or dangerous, which leaves them exposed to financial loss and identity theft. ScamShield AI solves this by giving anyone an instant, AI-powered second opinion on a suspicious message.

## 🧠 Approach
This project follows **Option 2 — Multi-Agent AI System**, built entirely on **n8n** and powered by **Google Gemini**. Instead of a single LLM call, the message passes through four specialized agents, each responsible for a distinct part of the analysis, with each agent's output feeding into the next.

**Architecture:**
```
User → Message Intelligence Agent → Scam Pattern Detector Agent → Risk Assessment Agent → Safety Advisor Agent → Final Result
```

## 🤖 Agent Roles

| Agent | Responsibility |
|---|---|
| **Message Intelligence** | Parses the incoming message and extracts its intent, tone, and key content |
| **Scam Pattern Detector** | Checks the extracted content against known scam/fraud patterns and tactics |
| **Risk Assessment** | Scores the overall risk level based on the detected patterns |
| **Safety Advisor** | Translates the risk score into clear, actionable safety advice for the user |

Each agent has a single, clearly defined job, and passes structured output forward to the next node in the chain — no agent duplicates another's work.

## 🛠️ Tech Stack
- **n8n** — workflow orchestration engine
- **Google Gemini** — LLM powering each agent's reasoning
- **Webhook** — entry point for incoming messages
- **Python (requests)** — lightweight test client

## ⚙️ How It Works
1. A message is sent via `POST` request to the **ScamShield Input** webhook.
2. The message flows sequentially through the four Gemini-powered agent nodes.
3. Each agent enriches the payload with its own analysis before passing it forward.
4. The workflow returns a structured JSON response summarizing the risk level and recommended action.

## 🚀 Setup & Usage
```bash
# 1. Import the workflow
Import ScamShield-AI-Workflow.json into your n8n instance

# 2. Add credentials
Add your Google Gemini API key to each Chat Model node

# 3. Publish
Click "Publish" in n8n to activate the production webhook

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the test client
python test_webhook.py
```

## 🎥 Demo

### n8n Workflow

The complete ScamShield AI workflow consists of four specialized AI agents:

User Message → Message Intelligence → Scam Pattern Detector → Risk Assessment → Safety Advisor → Final Result

### Successful Execution

The workflow was successfully executed through n8n, with all four AI agents processing the input sequentially.

### Sample Analysis

A test message is sent through the webhook and processed by all four agents. The final output contains the identified scam pattern, risk level, and recommended safety actions.

## ✨ What Makes This Project Unique
- A genuine multi-agent pipeline — not a single LLM prompt dressed up as "multi-agent." Each agent has a distinct, non-overlapping responsibility.
- Tackles a real, everyday risk that affects non-technical users.
- Structured hand-off of information between agents, so each stage builds on the last rather than repeating it.


