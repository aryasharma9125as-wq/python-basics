tasks = []

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print("Removed:", removed)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List Manager.")
        break

    else:
        print("Invalid choice. Please try again.")
