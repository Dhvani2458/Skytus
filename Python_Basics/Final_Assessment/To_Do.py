tasks = []
complete_tasks = []

while True:
    print("\n=======TO-DO LIST======")
    print("1. Add Task.")
    print("2. View Task.")
    print("3. Complete Task.")
    print("4. Delete Task.")
    print("5. Exit.")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("\nEnter a Task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("\nNo Tasks found.")
        else:
            print("\nYour Tasks: ")

            for i, task in enumerate(tasks , 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == (0):
            print("No Task found.")
        else:
            print("\nYour Tasks: ")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {tasks}")
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1] = "✓ " + tasks[number - 1]
                print("Task Completed!")
            else:
                 print("Invalid task number.")

    elif choice == "4":
            if len(tasks) == 0:
                print("No Task found.")
            else: 
                print("\nYour Tasks: ")

                for i,task in enumerate(tasks, 1):
                    print(f"{i}. {tasks}")

                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print(f"Deleted: {deleted_task}")
                else:
                    print("Invalid task number.")

    elif choice == "5":
            print("Goodbye!")
            break
    else:
         print("Invalid choice.")