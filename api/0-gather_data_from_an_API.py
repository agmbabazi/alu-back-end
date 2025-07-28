#!/usr/bin/python3
"""
Simple script to get an employee's completed tasks from the JSONPlaceholder API
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the user provided exactly one argument and it's a number
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Failed to fetch users data")
        sys.exit(1)
    users = users_response.json()

    # Find the employee name by id
    employee_name = None
    for user in users:
        if user['id'] == employee_id:
            employee_name = user['name']
            break

    if employee_name is None:
        print("User not found")
        sys.exit(1)

    # Fetch all todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Failed to fetch todos data")
        sys.exit(1)
    todos = todos_response.json()

    # Variables to count tasks
    total_tasks = 0
    completed_tasks = 0
    completed_titles = []

    # Loop through todos and check those belonging to the employee
    for todo in todos:
        if todo['userId'] == employee_id:
            total_tasks += 1
            if todo['completed']:
                completed_tasks += 1
                completed_titles.append(todo['title'])

    # Print the summary
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t {title}")

