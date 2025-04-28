# Multi-Agent ADK + LangChain Template

This template demonstrates a multi-agent system using Google ADK and LangChain. Agents are modular, async-ready, and can be extended for tool use, LLMs, and workflows.

## Project Structure
```
/agents/
    generator_agent.py   # Generates post content (LangChain)
    reviewer_agent.py    # Reviews and improves content (LangChain)
    poster_agent.py      # Posts to LinkedIn (API)
main.py                 # Orchestrates agents
requirements.txt        # Dependencies
.env                    # API keys and secrets
README.md
```

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Add your API keys (OpenAI, LinkedIn, etc.) to `.env`.

## Usage
Run the orchestrator:
```powershell
python main.py
```

## Extend
- Add more agents to `/agents/`.
- Use LangChain for LLMs, tools, or chains.
- Integrate ADK memory, toolsets, or web UI as needed.

