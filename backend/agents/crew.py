from crewai import Agent, Task, Crew

def run_crew(sleep, bio, memory):

    # AGENTS
    sleep_agent = Agent(
        role="Sleep Scientist",
        goal="Analyze sleep patterns",
        backstory="Expert in circadian rhythms and sleep science.",
        llm="ollama/llama3",
        verbose=True
    )

    bio_agent = Agent(
        role="Biological Analyst",
        goal="Analyze biological data",
        backstory="Specialist in human physiology and biomarkers.",
        llm="ollama/llama3",
        verbose=True
    )

    analyst = Agent(
        role="Health Strategist",
        goal="Combine insights",
        backstory="Experienced in integrating multi-domain health insights.",
        llm="ollama/llama3",
        verbose=True
    )

    risk_agent = Agent(
        role="Risk Evaluator",
        goal="Determine health risk level",
        backstory="Expert in identifying potential health risks and severity.",
        llm="ollama/llama3",
        verbose=True
    )

    recommendation_agent = Agent(
        role="Recommendation Optimizer",
        goal="Generate precise actionable advice",
        backstory="Specialist in creating optimized health improvement plans.",
        llm="ollama/llama3",
        verbose=True
    )

    # TASKS
    sleep_task = Task(
        description=f"Analyze sleep data: {sleep}",
        expected_output="Sleep insights",
        agent=sleep_agent
    )

    bio_task = Task(
        description=f"Analyze bio data: {bio}",
        expected_output="Bio insights",
        agent=bio_agent
    )

    analysis_task = Task(
        description="""
        Combine the sleep and bio insights.
        Identify patterns, root causes, and overall condition.
        """,
        expected_output="Detailed health analysis",
        agent=analyst,
        context=[sleep_task, bio_task]
    )

    risk_task = Task(
        description="""
        Based on the analysis, classify risk level as LOW, MEDIUM, or HIGH.
        """,
        expected_output="Risk level with reasoning",
        agent=risk_agent,
        context=[analysis_task]
    )

    recommendation_task = Task(
        description="""
        Based on analysis and risk level, give actionable recommendations.
        """,
        expected_output="Step-by-step advice",
        agent=recommendation_agent,
        context=[analysis_task, risk_task]
    )

    # CREW (🔥 FIXED INDENTATION)
    crew = Crew(
        agents=[
            sleep_agent,
            bio_agent,
            analyst,
            risk_agent,
            recommendation_agent
        ],
        tasks=[
            sleep_task,
            bio_task,
            analysis_task,
            risk_task,
            recommendation_task
        ],
        verbose=True
    )

    result = crew.kickoff()

    print("DEBUG RESULT:", result)

    return {"final_output": str(result)}
