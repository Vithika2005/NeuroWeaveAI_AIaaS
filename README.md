Multi-agent AI health analysis system using CrewAI + FastAPI + Ollama. 
Simulates distributed reasoning pipeline for sleep, bio analysis, risk detection, and recommendations.

# 🧠 NeuroWeave AI

**NeuroWeave AI** is a multi-agent health intelligence system that analyzes sleep and biological data to generate risk assessments and actionable recommendations.

Built using **CrewAI, FastAPI, and local LLMs (Ollama)**, it simulates a distributed AI reasoning pipeline where specialized agents collaborate to produce structured insights.

---

## 🚀 Features

* 🧠 **Multi-Agent AI System**

  * Sleep Scientist
  * Biological Analyst
  * Health Strategist
  * Risk Evaluator
  * Recommendation Optimizer

* 🔗 **Task Chaining Pipeline**

  * Sleep → Bio → Analysis → Risk → Recommendations

* ⚡ **FastAPI Backend**

  * REST API for real-time AI analysis

* 💾 **Local Storage System**

  * Simulated S3 (file storage)
  * Simulated DB (history logs)

* 🤖 **Local LLM Integration**

  * Powered by Ollama (no API cost)

* 📊 **Structured Output**

  * Analysis
  * Risk level
  * Report

---

## 🏗️ Architecture

```
User Input
    ↓
FastAPI Endpoint (/analyze)
    ↓
CrewAI Multi-Agent System
    ↓
Task Execution Pipeline
    ↓
Final Output
    ↓
Stored in Local Storage
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **AI Orchestration:** CrewAI
* **LLM:** Ollama (Llama3)
* **Storage:** Local JSON (simulating AWS)
* **Frontend (optional):** Streamlit

---

## 📂 Project Structure

```
neuroweave-ai/
│
├── backend/
│   ├── agents/
│   │   └── crew.py
│   ├── tools/
│   │   └── storage_tool.py
│   ├── main.py
│
├── frontend/
│   └── app.py
│
├── local_s3/
├── local_db/
└── README.md
```

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/neuroweave-ai.git
cd neuroweave-ai
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

---

## 🤖 Run Ollama (Local LLM)

```bash
ollama pull llama3
ollama run llama3
```

---

## ▶️ Run Backend

```bash
uvicorn backend.main:app --reload
```

Visit:
👉 http://127.0.0.1:8000/docs

---

## 🎨 Run Frontend (Optional)

```bash
streamlit run frontend/app.py
```

---

## 🧪 Example API Request

```json
POST /analyze

{
  "user_input": "slept 5 hours, high stress"
}
```

---

## 📤 Example Output

```json
{
  "analysis": "...",
  "guardrail": {
    "risk_level": "MEDIUM"
  },
  "report": "..."
}
```

---

## 🧠 How It Works

1. Sleep Agent analyzes sleep patterns
2. Bio Agent analyzes biological signals
3. Strategist combines insights
4. Risk Agent evaluates health risk
5. Recommendation Agent generates actionable advice

---

## 📌 Future Enhancements (V4)

* ☁️ AWS Integration (S3 + DynamoDB)
* 🐳 Docker Deployment
* 📊 MLflow Tracking
* 📡 Real-time Data Streaming
* 📈 Observability (Prometheus + Grafana)

---

## 👤 Author

Built by **Vithika Surve**

---

## ⭐ Why This Project Matters

NeuroWeave AI demonstrates how multi-agent systems can simulate real-world decision-making pipelines in healthcare—moving beyond single-model AI into collaborative intelligence systems.
