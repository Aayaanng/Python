from pathlib import Path

folder_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling")
file_path = folder_path / "test.txt"

with open(file_path, "r") as file:
    abc = file.read()
print(abc)
#read one line at a time
with open(file_path, 'r') as file:
    line = file.readlines()
print(line)
#removes /n this is better
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())
#read singular line
with open(file_path, 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
print(line1)
print(line2)