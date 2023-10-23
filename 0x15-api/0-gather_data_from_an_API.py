#!/usr/bin/python3

"""
This script uses a REST API to retrieve information about an employee's TODO list progress.
"""

import requests
import sys

def get_emp_todo_list_progress(emp_id):
    """
    Retrieve and display the employee's TODO list progress.

    Args:
        emp_id (int): The employee's ID.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, emp_id)
    todos_url = "{}/todos?userId={}".format(base_url, emp_id)

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task.get("completed")]
        total_tasks = len(todos_data)
        done_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(user_data['name'], done_tasks, total_tasks))
        for task in completed_tasks:
            print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]

    try:
        emp_id = int(emp_id)
        get_emp_todo_list_progress(emp_id)
    except ValueError:
        print("Please provide a valid integer as the employee ID.")

