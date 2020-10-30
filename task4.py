import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Pochacco!")
label3 = tk.Label(window, text=" A cuddly little puppy! This is from the same ", bg="#aaffff")
label4 = tk.Label(window, text="creators who bought you Keropi and Kero Kero", bg="#aaffff")

label1.Place()