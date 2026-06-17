import time
print("Hello")
time.sleep(2)
print("World")


import math
print(math.sqrt(10))
print(math.factorial(5))
print(math.pi)

import random
print(random.randint(1, 100))
print(random.choice(['apple', 'banana', 'cherry']))

import datetime
a = datetime.datetime.now()
print(a)

import os
print(os.getcwd())

import tkinter as tk
b = tk.Tk()
b.title("My First GUI")
b.geometry("300x200")
label = tk.Label(b, text="Hello, Tkinter!")
label.pack()