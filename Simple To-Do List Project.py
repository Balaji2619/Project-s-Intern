# Simple To-Do List Application
# Diploma Level Python Project

todo_list = []

print("Welcome to To-Do List Application")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View List")
    print("3. Remove Any Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task is added successfully.")

    elif choice == "2":
        if not todo_list:
            print("Your To-Do List is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not todo_list:
            print(" There Is No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(todo_list):
                removed_task = todo_list.pop(task_no - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Wait, that wasn't a valid number.")

    elif choice == "4":
        print("See You Later!")
        break

    else:
        print("Not an option Friend. Please select between 1 to 4.")
