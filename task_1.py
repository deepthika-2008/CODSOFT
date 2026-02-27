tasks = []
def show_menu():
    print("\n------ TO-DO LIST MENU ------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else " Not Done"
            print(f"{i+1}. {task['title']} - {status}")



def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!")



def update_task():
    view_tasks()
    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_title = input("Enter new task name: ")
            tasks[num-1]["title"] = new_title
            print("Task updated!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")


# Delete task
def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")


# Mark completed
def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number completed: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")


# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")