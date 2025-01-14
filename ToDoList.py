#This simple project allows you to add tasks, delete tasks, and view tasks.
# Define an empty list to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task deleted:", task)
    else:
        print("Task not found")

def view_tasks():
    if not tasks:
        print("No tasks in the list")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

while True:
    print("Options:")
    print("Enter 'add' to add a task")
    print("Enter 'delete' to delete a task")
    print("Enter 'view' to view tasks")
    print("Enter 'exit' to end the program")

    user_input = input(": ")

    if user_input == "exit":
        break
    elif user_input == "add":
        task = input("Enter a task: ")
        add_task(task)
    elif user_input == "delete":
        task = input("Enter the task to delete: ")
        delete_task(task)
    elif user_input == "view":
        view_tasks()
    else:
        print("Invalid input")