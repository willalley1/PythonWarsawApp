import tkinter as tk
import os 
import math
import warsawFunc as funct

user="Paige"

root = tk.Tk()
root.geometry('800x800')
root.title("Warsaw Wireless")
root['bg']='orange'

frame0 = tk.Frame(root, height=100, width=800, bg="orange", padx=5, pady=5)
frame0.place(x=0, y=0)

frame1 = tk.Frame(root, height=700, width=800, bg="black", padx=5, pady=5)
frame1.place(x=0, y=101)


label0 = tk.Label(text=f"Hello, {user}", bg="orange")
label0.place(x=400,y=10)

addSale = tk.Button(root, text="Add Sale", width=15)
addSale.place(x=200, y=720)

root.mainloop()