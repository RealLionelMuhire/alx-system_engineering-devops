#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

import requests
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])

    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{emp_id}')
    if user_response.status_code != 200:
        print(f"Error: Employee with ID {emp_id} not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data['username']

    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')
    todos_data = todos_response.json()

    user_info = {
        emp_id: [{"task": task['title'], "completed": task['completed'], "username": username} for task in todos_data]
    }

    json_file_name = f"{emp_id}.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(user_info, json_file, indent=4)
