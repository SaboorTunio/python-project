import click # to create a cli
import json # to save and load task fromm a file
import os # to check if the file exists

TODO_FILE = "todo.json"


# Function to load tasks from the JSON file
def load_tasks ():
    if not os.path.exists(TODO_FILE): #check if file exists
        return [] # if not, return an empty list
    with open(TODO_FILE,"r") as file: # open the file in read mode
        return json.load(file) # Load and reurn the JSON data as a python list


# Function to save task to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE,"w") as file: # open the file in write mode
        json.dump(tasks,file, indent=4)  # Save task as formatted JSON


@click.group() # Define a Click command group (main CLI)
def cli():
    """Simple TOdo List Manager""" # Docstring for the CLI
    pass # No action , acts as a container for commands


@click.command() # Define a command called 'add'
@click.argument("task") # Accepts a required argument (tsak name)
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks() # Load existing task
    tasks.append({"task":task,"done":False}) # Append a new task (default: not done)
    save_tasks(tasks) # Save the up[date tasks]
    click.echo(f"Task added successfully: {task}") # Print a success message
    
  
@click.command()
def list():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No task found.")
        return
    for index, task in enumerate(tasks ,1):
        status ="✅"  if task['done'] else '❌'
        click.echo(f"{index}. {task['task']} [{status}]") 
  
  
@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks =load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number -1]["done"]=True
        save_tasks(tasks)
        click.echo(f"{task_number} marked as completed.")
    else:
        click.echo(f"Invalid task number : {task_number}")
@click.command()
@click.argument("task_number",type=int)
def remove(task_number):
    '''Remove task from the list'''
    tasks =load_tasks()
    if 0<task_number <= len(tasks):
        remove_task =tasks.pop(task_number - 1)
        save_tasks(tasks) # Save update tasks
        click.echo(f"removed task :{remove_task['task']}")
    else:
        click.echo(f"invalid task number")            
        
# Add commands to the main CLI group  
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

# If the script is run directly, start the CLI
if __name__=="__main__":
    cli()
    