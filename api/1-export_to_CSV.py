#!/usr/bin/env python3

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
