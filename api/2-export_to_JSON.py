import sys
import requests
import json

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = employee_data.get('id')
    username = employee_data.get('username')

    # Get employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_list = response.json()

    # Prepare JSON data
    json_data = {str(user_id): [{"task": task.get('title'), "completed": task.get('completed'), "username": username} for task in todo_list]}

    # Write data to JSON file
    filename = f"{user_id}.json"
    with open(filename, mode='w') as file:
        json.dump(json_data, file, indent=4)

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
 