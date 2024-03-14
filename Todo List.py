def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    print("\n--- Tasks ---")
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index+1}. {task['task']} - {status}")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to mark as completed: ")) - 1
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to delete: ")) - 1
        del tasks[task_index]
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()
