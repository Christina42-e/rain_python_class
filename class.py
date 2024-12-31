class Person:## blueprint
   def__int__(self, name, age): # dunder method or magic :self  call, __init__: runs when object create
        self.name = name
        self.age = age


    # def__init__(self):
    #   pass
    # pass

kristina = person("Kristina", 17)

print(kristina.name)
print(kristina.age)


class PhoneFactory:
    model:None
    color:None
    is_android: None

    def __init__(self, model, color, is_android):
        self.model = model
        self.color = color
        self.is_android = is_android
        print("Phone created")

    def_str_(self):
        return f"{self.model}.{self.color}"

    def check_os(self):
        if self.is_android:
            print("Android")
        
        else:
            print("ios")



## Todo  List using python class and object
class TodoList:
    def__init__(self):
        self.tasks = []

def add_task(self,task):   ##Create
   self.tasks.append(task)
   print(f"Task '{task}' added to the list.")


def remove_task(self, task):##  Delete
   if  task in self tasks:
       self_tasks.remove(task)
       print(f"Task '{task}' removed from the list.")

    else:
        print(f"Task '{task}' not found in the list.")

def  update_task(self, old_task, new_task): ##Update
    if old_task in self tasks:
        index = self tasks index(old_task)
        self tasks[index] = new_task
        print(f"Task updated to '{new_task}'")
    else:
        print(f"Task '{old_task}' not found in the list")

def show_tasks(self):   ## Get
    if self tasks:
        print("Yout Todo List:")
        for index, task in enumerate(self tasks):
            print(f"(index + 1).{tasks}")

    else:
        print("Your Todo List is empty.")

todo_list = TodoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Finish the report")
todo_list.update_task("Buy groceries", "Go for a walk")
todo_list.show_tasks()

Task 'Buy groceries' added to the list
Task 'Finish the report' added to the list.
Task 'Call mom' added to the list
Your Todo List:
1.  Buy groceries
2.  Finish the report
3.  Call mom