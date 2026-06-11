#1 
from pathlib import Path

folder_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling")
file_path = folder_path / "test.txt"
with open(file_path,'r') as file:
    abc = file.read()
print(abc)
#2
with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")
#