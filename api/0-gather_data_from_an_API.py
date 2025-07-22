#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
