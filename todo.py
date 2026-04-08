tasks = []

while True:

    print("\n--- TO DO LIST APPLICATION ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available")

        else:
            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete")

        else:
            num = int(input("Enter task number to delete: "))

            if num > 0 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted successfully")

            else:
                print("Invalid task number")

    elif choice == "4":

        print("Thank you! Exiting application")
        break

    else:
        print("Invalid choice, try again")



