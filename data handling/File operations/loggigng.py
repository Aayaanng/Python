from datetime import datetime
from pathlib import Path

file_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling\log.txt")

def log_action(message):
    """Write a timestamped message to the log file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{timestamp}] {message}\n'

    with open(file_path, 'a') as log_file:
        log_file.write(log_entry)

log_action('Program started')

name = input('Enter your name: ')
log_action(f'User entered name: {name}')

log_action('Program finished successfully')