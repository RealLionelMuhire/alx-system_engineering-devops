#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            employee_id = i.get('id')
            employee_name = i.get('name')

    user_tasks = []

    for i in data:
        if i.get('userId') == int(argv[1]):
            total += 1

            task_info = {
                "task": i.get('title'),
                "completed": i.get('completed'),
                "username": employee_name
            }

            user_tasks.append(task_info)

    user_data = {str(employee_id): user_tasks}
    json_output = json.dumps(user_data, indent=2)

    json_file_name = "{}.json".format(employee_id)

    with open(json_file_name, 'w') as json_file:
        json_file.write(json_output)
