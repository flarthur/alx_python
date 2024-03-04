#!/usr/bin/python3
import json
import requests
from sys import argv


def fetch_employee_tasks(user_id):
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': user_id}
    response = requests.get(url, params=params)
    tasks = response.json()
    return tasks


def export_to_json():
    all_tasks = {}
    for user_id in range(1, 11):  # Assuming user IDs range from 1 to 10
        tasks = fetch_employee_tasks(user_id)
        all_tasks[str(user_id)] = [
            {"username": task["userId"], "task": task["title"], "completed": task["completed"]}
            for task in tasks
        ]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_to_json()
