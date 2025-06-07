"""
users can choose to :
Add tasks
View tasks -and in these be able to choose a task to mark as completed/delete it
Delete tasks-batch delete
Save tasks
Load tasks
Quit application -can save their tasks before
"""
from datetime import datetime
import json
from enum import Enum
import os
import random


class TaskState(Enum):
    PENDING="PENDING"
    COMPLETED="COMPLETED"

class Task:
    def __init__(self,body) -> None:
        self.body=body
        self.state=TaskState.PENDING
    
    def mark_task(self):
        if self.state==TaskState.PENDING:
            self.state=TaskState.COMPLETED
        else:
            self.state=TaskState.PENDING
        print("Succesful marking")
        

class App:
    def __init__(self):
        self.task_manager=TaskManager()
        
    def navigate_back(self):
        while True:
            option=input("Type 'M' to go back to main menu")
            
            if option =="M":
                return self.main_menu()
        
    def view_input_validation(self,choice,length):
        
            if choice =="M":
                self.main_menu()
                
            elif choice.isdigit():
                choice=int(choice)
                choice-=1
                if choice<length and choice>=0:
                    self.task_manager.manage_task(choice)
            else:
                print("Invalid choice")
                self.task_manager.view_tasks()
            # self.main_menu() 
    def main_menu(self):
        print("Hello welcome to this task manager app")
        print("Enter a letter to choose an option:")
        print(" 'A' - Add new tasks")
        print(" 'V' - View tasks (and manage them)")
        print(" 'D' - Delete multiple tasks")
        print(" 'S' - Save your tasks")
        print(" 'L' - Load tasks from a file")
        print(" 'Q' - Quit the application (you'll be asked to save first)")
        while True:
            choice=input("> ")
            match choice:
                case 'A':
                    print("You chose to Add new tasks.")
                    self.task_manager.add_task()
                    self.navigate_back()
                case 'V':
                    print("You chose to View tasks.")
                    choice,length=self.task_manager.view_tasks()
                    self.view_input_validation(choice,length)

                case 'D':
                    print("You chose to Delete multiple tasks.")
                    value=self.task_manager.batch_delete()
                    if value==0:
                        self.navigate_back()
                case 'S':
                    print("You chose to Save your tasks.")
                    save_json(self.task_manager.tasks)
                    self.navigate_back()
                case 'L':
                    print("You chose to Load tasks.")
                    loaded_data=self.task_manager.load_json()
                    print("it returned the loaded data")
                    print(loaded_data)
                    self.task_manager.add_json_tasks(loaded_data)
                    self.main_menu()

                    # Code for loading tasks
                case 'Q':
                    print("You chose to Quit the application.")
                    pick=self.quit_game()
                    if pick=="Y":
                        break
                    else:
                        self.main_menu()        
                case _: # This is the "default" case, similar to 'else'
                    print("Invalid choice. Please try again.")
                    break
    
    def quit_game(self):
        print("Are you sure you want to quit? Make sure you've saved your tasks ")
        choice=input("Press 'Y' if yes and any other key to return")
        return choice
        
           

class TaskManager:
    def __init__(self):
        self.tasks=[]

    def add_task(self):
        task=Task(input("Please enter a task you to do: "))
        
        self.tasks.append(task)
        return self.tasks
    def add_json_tasks(self,loaded_data):
        for data_body,data_state in loaded_data.items():

            task=Task(data_body)
            # print(task.body,str(task.state))
            # task.state=i
            print(data_state)
            if data_state=="TaskState.PENDING":
                task.state=TaskState.PENDING
            else:
                task.state=TaskState.COMPLETED

            # print(str(task.state))
            self.tasks.append(task)

    def view_tasks(self):
        
        print("--Your tasks are as below--")
        if self.tasks==[]:
            print("Empty list of tasks. Create tasks to get access to them")
            
        for i,task in enumerate(self.tasks):
            print(f"{i+1}: {task.body} it's state is {task.state} ")
        print("Type the number of the task to access it and manage it")
        choice=input("or type 'M' to go back to main menu")
        return choice,len(self.tasks)

          
    def manage_task(self,choice):
        
            print(F"{self.tasks[choice].body} has the state {str(self.tasks[choice].state)}")
            print("Type 'M' to mark or unmark, 'D' to delete it or 'B' to go back to viewing the rest of the tasks ")
            verdict=input("> ")
            match verdict:
                case 'M':
                    self.tasks[choice].mark_task()

                    
                case 'D':
                    print("You chose to Delete task.")
                    del self.tasks[choice]
                    
                case 'B':
                    print("You chose to go back to viewing tasks.")
                    self.view_tasks()

                    
                    
                case _: 
                    print("Invalid choice. Try again.")
    def load_json(self):
        try:
            all_entries = os.listdir("saved_tasks")
            for i,entry in enumerate(all_entries):
                print(f"{i+1}: {entry}")

        except Exception :
            print("You dont have saved tasks folder/directory")
        while True:
            file_path_index=int(input("enter the number of the file you want to load"))
            file_name=all_entries[file_path_index-1]
            file_path=os.path.join("saved_tasks",file_name)
            try: 
                with open(file_path,"r")as f:
                    loaded_data=json.load(f)
                    
                    return loaded_data
            except FileNotFoundError:
                print(f"Error: File at {file_path} not found")
            except Exception:
                print("Error on decoding the file or other loading related errors")
    

    def batch_delete(self):
        print("Are you sure you want to delete all tasks? ")
        choice=input("Press 'Y' if you are and any other key if you are not ")
        if choice=="Y":
            self.tasks.clear()
        return 0

def save_json(tasks):
    files_directory="saved_tasks"
    time_now=datetime.now()
    formatted_timestamp = time_now.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"tasks_{formatted_timestamp}.json"
    file_path=os.path.join(files_directory,file_name)
    try:
        with open(file_path,"w")as f:
            formatted_tasks={}

            for task in tasks:
                formatted_tasks[task.body]=str(task.state)
            print(formatted_tasks)
            json.dump(formatted_tasks, f, indent=4)
        print(f"\nData successfully written to {file_path}")
    except Exception as e:
        print(f"Unexcpected Error {e}")
        
    
  
main_app=App()  
main_app.main_menu()
        

