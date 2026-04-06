from agents.crew import run_crew

sleep = {"sleep_quality": "Poor Sleep"}
bio = {"cluster": "Balanced Health Cluster"}

result = run_crew(sleep, bio, "")

print(result)
