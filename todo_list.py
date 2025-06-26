"""
Simple CLI To-Do List
Add, view, and remove tasks from your to-do list.
"""

tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            idx = int(input("Enter the task number to remove: "))
            if 1 <= idx <= len(tasks):
                removed = tasks.pop(idx - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
