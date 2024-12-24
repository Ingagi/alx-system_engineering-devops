#!/usr/bin/python3
""" Gather data from an API """

import requests
from sys import argv
"""modules to work with"""

def get_employee_todos_progress(employee_id):
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get9url + f"users/(employee_id)")
        user_data = user_datas.json()
        employee_name = user_data['name']

        """fetch todos list for the employee"""
        todo_list = requests.get(url + f"todos?userId-(employee_id)")
        json_todos_list = len(task_done)

        """display the result"""
        print(f"employee {employee_name} is done with tasks("
                f"{no_task_done}/{total_task}):")

        """title of completed task"""
        for task in task_done:
            print(f"\t {task['title']}")
    except Exception as e:
        print(f"an error occured: {e}:)


if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: script <employee_id>")
        else:
        get_eployee_todos_progress(argv[1])

