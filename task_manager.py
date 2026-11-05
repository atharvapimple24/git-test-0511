# task_manager.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(task_name):
    tasks.append(task_name)
    print(f"Added task: '{task_name}'")

if __name__ == "__main__":
    print("--- Task Tracker ---")
    add_task("Learn Git basics")
    add_task("Push code to GitLab")
    show_tasks()

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed task: '{removed}'")
    else:
        print("Invalid task index.")