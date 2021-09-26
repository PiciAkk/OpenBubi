import sys
sys.path.append("../")
import openbubi
import tkinter as tk
from tkinter import messagebox
import json
import threading
from os import system as runcmd

map = openbubi.BubiMap()
user = openbubi.BubiUser(sys.argv[1], sys.argv[2])

selectedBike = 0
def rentBike():
    user.rentBike(selectedBike)
def selectBike(selection):
    selectedBike = selection
def enterLocation():
    nameOfNearestStation = map.getNearestStationByAddress(locationField.get())
    messagebox.showinfo("Legközelebbi állomás", nameOfNearestStation)
    defaultValue = tk.StringVar(root)
    defaultValue.set("Válassz ki egy biciklit")
    bikes = map.listAllBikesOnStation(nameOfNearestStation)
    bikeNumbers = []
    for i in json.loads(bikes):
        bikeNumbers.append(i["number"])
    try:
        bikeList = tk.OptionMenu(root, defaultValue, *bikeNumbers, command=selectBike)
        bikeList.pack()
        rentBTN = tk.Button(root, text="Bicikli bérlése", command="rentBike")
        rentBTN.pack()
    except:
        messagebox.showerror("Hiba!", "Nincs bicikli a beírt lokációhoz legközelebbi állomáson")
root = tk.Tk()
root.title("Főképernyő")
root.geometry("500x200")
messagebox.showinfo("Helló!", "Köszöntelek, " + user.getScreenName() + "!")
locationLabel = tk.Label(root, text="Adj meg egy lokációt")
locationLabel.pack()
locationField = tk.Entry(root)
locationField.pack()
locationBTN = tk.Button(root, text="Kész", command=enterLocation)
locationBTN.pack()
root.mainloop()
