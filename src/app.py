# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from accounts import accounts
from accounts import add_account, login
from tasks import create_task, delete_task
from tasks import delete_all_tasks, mark_as_finished, todo_list

if __name__ == "__main__":
    """
        Allow a person to input a name and a password

        E.g
    """
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    """
        Let the person sign in. If there details do not exist,
        create an account for them

        E.g
    """
    if not login(name, password):
        add_account(name, password)

    """
        Provide options:
            1. creating a task
            2. deleting a task
            3. deleting all tasks
            4. Marking a task finished

        E.g
    """

    print("Select Option:")
    print("1: Create Task")
    print("2: Delete A Task")
    print("3: Mark a task as finished.")
    print("4: Delete All Tasks")

    selection = int(input("selection: "))

# Code that implements the selected option

    if selection == 1:
        task = input('Enter the name of the task to create: ')
        create_task(task)

    if selection == 2:
        task = input('Enter the name of the task to delete: ')

    if selection == 3:
        task = input('Enter the name of the task to mark as finished: ')

    if selection == 4:
        delete_all_tasks()