#!/usr/bin/env python3

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
