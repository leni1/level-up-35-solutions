# --- tasks.py ---
# This file contains code that manages your todo_list

todo_list = []

# A function creates a task

def create_task(task):
    """
    Adds the task (string value) to todo_list
    """
    todo_list.append(task)

# A function deletes a task

def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    for item in todo_list:
        if task == item:
            todo_list.remove(item)
    print(todo_list)

# A function that marks a task finished

def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    for item in todo_list:
        if task == item:
            if '[finished]' in item:
                print('Task is finished')
            item += '[finshed]'
    print('Task marked as complete.')

# A function that deletes all tasks

def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    todo_list = []
