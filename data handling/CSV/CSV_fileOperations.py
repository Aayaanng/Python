#Reading csv files
import csv
from pathlib import Path

file_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling\CSV\data.csv")
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)  # DictReader gives each row as a dict
    for row in reader:
        print(f"{row['name']} from {row['city']} scored {row['score']}")
#appending  csv file
new_students = [
    ['David',   12, 'Bangalore', 85],
    ['Eva',     11, 'Pune',      90],
]
with open(file_path, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_students)