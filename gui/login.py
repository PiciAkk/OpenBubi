import tkinter as tk
from tkinter import messagebox
import threading
from os import system as runcmd

root = tk.Tk()
root.title("Bejelentkezés")
def openMainScreen():
    runcmd("python mainscreen.py " + phoneField.get() + " " + passwordField.get())
def login():
    mainScreenThread = threading.Thread(target=openMainScreen)
    mainScreenThread.start()
phoneField = tk.Entry(root, width=15)
phoneField.pack()
passwordField = tk.Entry(root, show="*", width=15)
passwordField.pack()
loginBTN = tk.Button(root, text="Bejelentkezés", command=login)
loginBTN.pack()
root.mainloop()
