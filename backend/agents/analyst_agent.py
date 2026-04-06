import json

def analyst_agent(sleep_result, bio_result, memory_context=""):
    prompt = f"""
You are a Biological Intelligence Analyst.

Return ONLY valid JSON.

Sleep:
{sleep_result}

Bio:
{bio_result}

Memory:
{memory_context}

Output format:
{{
  "insight": "...",
  "root_cause": "...",
  "pattern": "...",
  "risk": "LOW | MODERATE | HIGH",
  "recommendation": "..."
}}
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except:
        return {"error": response}
