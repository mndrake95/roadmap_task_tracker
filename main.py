
import json
import os
from datetime import datetime
from datetime import timezone

time_format = "%Y-%m-%dT%H:%M:%S"

class Task:
    __no_of_tasks = 0

    def __init__ (self, description, *args, **kwargs):
        Task.__no_of_tasks += 1
        self.id = self.__no_of_tasks
        self.description = description
        self.status = "not-done"
        self.created_at = str(datetime.now(timezone.utc))
        self.updated_at = self.created_at

        for key, val in kwargs.items():
            if key == "description":
                self.description = val
            if key == "status":
                self.status = val
            if key == "created_at" and val is not None:
                self.created_at = val
            if key == "updated_at" and val is not None:
                self.updated_at = val
                
    def display_info(self):
        print(f"Task ID: {self.id}, Description: {self.description}, Status: {self.status}, Created: {self.created_at}, Updated: {self.updated_at}")

    def 

if __name__ == "__main__":
    while True:
        print ("\n")
        print ("Choose an action:")
        print ("----------------------")
        print ("1. Add task")
        print ("2. Update task")
        print ("3. List tasks")
        print ("4. Change task status")
        print ("5. Delete task")
        print ("6. Exit")

        choice = input("Choose # of action: ")

        if (choice == "1"):
            my_task_manager.add_task()
        elif (choice == "2"):
            my_task_manager.delete_task()
        elif (choice == "3"):
            my_task_manager.list_task()
        elif (choice == "4"):
            my_task_manager.task_status_change()
        elif (choice == "5"):
            break
        else:
            print ("Invalid input. Please enter # of action from 1 to 5.")

    print ("You exited.")
    