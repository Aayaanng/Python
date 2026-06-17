import tkinter as tk
win = tk.Tk()
y = 0

def tkinter():
    global y
    y += 1
    print(y)

win.geometry("300x200")
b = tk.Button(
    win,
    text="Click Me",
    command=tkinter
)
b.pack()
win.mainloop()