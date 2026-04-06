
from fastapi import FastAPI
from pydantic import BaseModel
from agents.crew import run_crew

app = FastAPI()

class InputData(BaseModel):
    user_input: str

@app.post("/analyze")
def analyze(data: InputData):

    result = run_crew(
        sleep=data.user_input,
        bio="default bio",
        memory="default memory"
    )

    return {
        "analysis": result,
        "guardrail": {
            "risk_level": "MEDIUM"
        },
        "report": result
    }
