import os
print("Curent Working Directory:", os.getcwd())
with open("test.txt", "r", encoding="cp1252") as f:
    x = f.read()