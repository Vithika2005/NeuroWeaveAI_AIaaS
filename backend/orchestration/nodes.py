from agents.sleep_agent import sleep_agent
from agents.bio_agent import bio_agent
from agents.analyst_agent import analyst_agent
from agents.guardrail_agent import guardrail_agent
from agents.report_agent import report_agent
from agents.planner import planner_agent
from agents.crew import run_crew
from tools.storage_tool import upload_report, store_user_data

#Report node 
def report_node(state):
    report = state["analysis"]

    # 💾 SAFE STORAGE (FREE)
    upload_report(report)
    store_user_data(report)

    return {"report": report}

#CrewAI 
def analyst_node(state):
    result = str(run_crew(
        state["sleep_result"],
        state["bio_result"],
        state.get("memory", "")
    ))
    return {"analysis": result}

#Planner Node
def planner_node(state):
    plan = planner_agent(state["user_input"])
    return {"plan": plan}

# 💤 Sleep Node
def sleep_node(state):
    result = sleep_agent(state["sleep_data"])
    return {"sleep_result": result}


# 🧬 Bio Node
def bio_node(state):
    result = bio_agent(state["bio_data"])
    return {"bio_result": result}

# ⚠️ Guardrail Node
def guardrail_node(state):
    guard = guardrail_agent(state["analysis"])
    return {"guardrail": guard}

