import sys
import requests

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Get employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_list = response.json()

    # Calculate completed tasks
    completed_tasks = [task for task in todo_list if task.get('completed')]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_list)

    # Print employee's progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
    for task in completed_tasks:
        print(f"     {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_info(employee_id)
