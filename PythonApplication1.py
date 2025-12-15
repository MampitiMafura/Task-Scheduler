import heapq
import datetime
import os

# Task Class

class Task:
    def __init__(self, description, due_date, priority, estimated_time):
        self.description = description
        self.due_date = due_date
        self.priority = int(priority)  # Higher number = higher priority
        self.estimated_time = estimated_time

    def __lt__(self, other):
        return self.priority > other.priority  # This ensures heapq compares by priority (highest first)

    def __str__(self):
        return (f"Task: {self.description} | Due Date: {self.due_date} | Priority: {self.priority} | Estimated Time: {self.estimated_time}\n")



# Scheduler Class

class Scheduler:
    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        heapq.heappush(self.tasks, task)
        print("Task added successfully!\n")


    def get_next_task(self):
        if self.tasks:
            next_task = heapq.heappop(self.tasks)
            print("Next Task (Highest Priority):")
            print(next_task)
        else:
            print("No tasks available.\n")


    def print_task_list(self):
        if not self.tasks:
            print("No tasks in the scheduler.\n")
            return
        print("All Tasks:")
        for task in sorted(self.tasks, reverse=True):
            print(task)


    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for task in sorted(self.tasks, reverse=True):
                f.write(f"{task.description},{task.due_date},{task.priority},{task.estimated_time}\n")
        print(f"Tasks saved to '{filename}' successfully!\n")


    def read_from_file(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    description, due_date, priority, estimated_time = line.strip().split(",")
                    task = Task(description, due_date, int(priority), estimated_time)
                    heapq.heappush(self.tasks, task)
            print(task)
        except FileNotFoundError:          #error handling for file not found
            print(f"File '{filename}' not found.\n")


# Main Menu

def main():
    scheduler = Scheduler()

    while True:
        print("========== TASK SCHEDULER ==========")
        print("1. Add Task")
        print("2. View Next Task")
        print("3. View All Tasks")
        print("4. Save Tasks to File")
        print("5. View Tasks from File")
        print("6. Exit")
        print("===================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            desc = input("Enter task description: ")
            due = input("Enter due date (YYYY-MM-DD): ")

            #date validation
            if len(due.split("-")) != 3:
                print("Please use the format YYYY-MM-DD.\n")
                continue

            prio = input("Enter priority (higher number = higher priority): ")
            time = input("Enter estimated time to complete (e.g. 2 hours): ")
            scheduler.add_task(Task(desc, due, prio, time))

        elif choice == "2":
            scheduler.get_next_task()

        elif choice == "3":
            scheduler.print_task_list()

        elif choice == "4":
            scheduler.save_to_file()

        elif choice == "5":
            scheduler.read_from_file()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.\n")



# Run the Application
main()

