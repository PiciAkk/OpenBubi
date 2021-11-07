import sys
sys.path.append("../")
import openbubi
from tkinter import *
import json
import datetime
from tkhtmlview import HTMLLabel

root = Tk()
root.title("BubiNews")

Label(root, text="BubiNews", font=("Helvetica", 20)).pack()

helpers = openbubi.BubiHelpers()
news = json.loads(helpers.getNewsFormatted())

for i in news:
    currentTitle = i["title"]
    currentDate = i["created_time"]
    currentURL = i["url_webview"]
    currentDate = datetime.datetime.fromtimestamp(currentDate).strftime('%Y-%m-%d %H:%M:%S')
    headerLabel = HTMLLabel(root, html=f"<a style='font-size: 12px' href='{currentURL}'><p style='text-align: center'>{currentTitle}</p></a>", width=100, height=1.5)
    dateLabel = Label(root, text=f"({currentDate})", font=("Helvetica", 10))
    headerLabel.pack()
    dateLabel.pack()

root.mainloop()