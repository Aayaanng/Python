from datetime import datetime
from pathlib import Path

file_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling\todo-list.txt")

def log_action(message):
    """Write a timestamped message to the log file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{timestamp}] {message}\n'

    with open(file_path, 'a') as log_file:
        log_file.write(log_entry)

log_action('Program started')
print("1 = add new task")
print("2 = read all task")
print("3 = mark a task as done")
print("4 = Quit")
a = input("Enter a choice")

if a == "1":
    task = input('Enter your task: ')
    log_action(f'User entered task: {task}')

if a == "2":
    with open(file_path, 'r') as log_file:
        abc = log_file.read()
    print(abc)

if a == "3":
    log_action('Task marked as done')
    with open(file_path, 'r') as log_file:
        abc = log_file.read()
    print(abc)
if a == "4":
    log_action('Program finished successfully')