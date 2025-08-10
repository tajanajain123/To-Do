import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    save_tasks(tasks)
                    print("Task removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
