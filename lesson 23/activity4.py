tasks = []

while True:
    print("\n1. Add task")
    print("2. View task")
    print("3. Quit")

    choice = input("Choose: ")

    if choice =="1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice =="2":
        if not tasks:
         print("No tasks yet")
        else:
           for i , task in enumerate(tasks, start=1):
            print(i, task)

           elif choice == "3":
    print("Goodbye")