import json
from pathlib import Path

file_path = Path(r"C:\Users\aayaa\OneDrive\Desktop\rancholabs\data handling\JSON\data.json")
data = {
    "course": "Python",
    "students": [
        {"name": "Alice", "score": 88},
        {"name": "Bob",   "score": 75}
    ]
}
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)  # indent=4 makes it readable
with open(file_path, 'r') as file:
    loaded = json.load(file)
print(loaded['course'])              
print(loaded['students'][0]['name']) 