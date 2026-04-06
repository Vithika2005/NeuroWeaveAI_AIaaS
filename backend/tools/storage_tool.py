from memory.vector_store import add_to_memory

def store_analysis(text):
    add_to_memory(text)

import json
import os

def upload_report(data):
    os.makedirs("local_s3", exist_ok=True)

    with open("local_s3/report.json", "w") as f:
        json.dump({"report": str(data)}, f, indent=2)


def store_user_data(data):
    os.makedirs("local_db", exist_ok=True)

    with open("local_db/history.json", "a") as f:
        f.write(json.dumps({"data": str(data)}) + "\n")
