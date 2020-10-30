import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

entry1 = tk.Entry(window, text="number 1")
label1 = tk.Label(window, text="x", borderwidth=4,)
entry2 = tk.Entry(window, text="number 2")
button1 = tk.Button(window, text="=")
entry3 = tk.Entry(window,text="solved")



entry1.grid(row=1, column=1)
label1.grid(row=1, column=2)
entry2.grid(row=1, column=3)
button1.grid(row=1, column=4)
entry3.grid(row=1, column=5)

window.mainloop()
