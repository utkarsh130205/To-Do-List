import os
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "completed": status == "True"})
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['completed']}\n")

def add_task(tasks):
    """Add a new task to the to-do list."""
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{idx}. {task['task']} - {status}")

def complete_task(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            print(f"Task '{tasks[task_index]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Exiting program.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
