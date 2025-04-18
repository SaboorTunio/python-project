import click # to create a cli
import json # to save and load task fromm a file
import os # to check if the file exists

TODO_FILE = "todo.json"

def load_tasks