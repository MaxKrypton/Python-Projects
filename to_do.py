tasks = []

def addtask():
    task = input("What is your new task? ")
    tasks.append(task)
    print("\n")
    print(f"New Task has been saved ##\n {task}")
    print("-------------------------------")

def removetask():
    for task in tasks:
        print(task)
    tasktoremove = int(input("Select the task you would like to remove: "))
    try:
        if  tasktoremove >= 0 and tasktoremove < len(tasks):
            tasks.pop(tasktoremove)
            print(f"The task number {tasktoremove}")
    except:
        print("Please Enter a Valid Number")

def viewlist():
    if not tasks:
        print("There are no tasks!!")
    else:
        for index, task in enumerate(tasks):
            print("\n")
            print("-----------------------")
            print(f"Task #{index}. {task}")
            print("-----------------------")

while True:
    print("Welcome to your Todo list :)")
    print("\n")
    print("What would you like to do?")
    print("----------------------------")
    print("1. Save a new task")
    print("2. Remove a task")
    print("3. List of tasks to do")
    print("4. Quit the program")
    try:
        choice = int(input("Select The number: "))
        
        if choice == 1:
            addtask()
            
        elif choice == 2:
            removetask()
            
        elif choice == 3:
            viewlist()
            
        elif choice == 4:
            break
        else:
            print("Invalid Input")
    except:
        print("Error: Invalid Input")