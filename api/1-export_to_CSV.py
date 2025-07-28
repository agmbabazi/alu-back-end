#!/usr/bin/env
"""
Export employee TODO list to CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Validate command line argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Failed to get todos")
        sys.exit(1)

    todos = todos_response.json()

    # Write to CSV file
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

    print(f"Data exported to {filename}")

