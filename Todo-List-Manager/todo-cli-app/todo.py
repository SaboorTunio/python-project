import click # to create a cli
import json # to save and load task fromm a file
import os # to check if the file exists

TODO_FILE = "todo.json"

def load_tasks ():
    if os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE,"r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE,"w") as file:
        json.dump(tasks,file, indent=4)    

@click.group()
def cli():
    """Simple TOdo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks
    tasks.append({"task":task,"done":False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")
    
cli.add_command(add)