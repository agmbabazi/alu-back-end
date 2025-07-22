#!/usr/bin/env python3
# Script to export employee TODO list to JSON format

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user = requests.get(f"{base_url}/users/{user_id}").json()
    username = user.get("username")

    # Fetch TODO list for the user
    todos = requests.get(f"{base_url}/todos", params={"userId": user_id}).json()

    # Prepare data for export
    tasks = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    } for task in todos]

    export_data = {user_id: tasks}

    # Write to JSON file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(export_data, json_file)
🔧 How to Run
bash
Copy
Edit
python3 2-export_to_JSON.py 2
cat 2.json
You’ll get something like:

json
Copy
Edit
{
  "2": [
    {
      "task": "suscipit repellat esse quibusdam voluptatem incidunt",
      "completed": false,
      "username": "Antonette"
    },
    {
      "task": "distinctio vitae autem nihil ut molestias quo",
      "completed": true,
      "username": "Antonette"
    },
    ...
  ]
}
