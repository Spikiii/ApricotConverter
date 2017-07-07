import tkinter as tk
from tkinter import filedialog as tkf
import csv
import os

#Inits
fp = ".."
data = []

#Settings

def openFile():
    global filePath, fp
    fp = tkf.askopenfilename(title = "Select file", filetypes = (("csv Files", "*.csv"), ("All Files", "*.*")))
    filePath.set(fp)

def leave():
    exit()

def showHelp():
    helpmes = "To do"
    top = tk.Toplevel()
    top.title("How to use this application")
    msg = tk.Message(top, text=helpmes)
    msg.pack()

#Setting up the tk window
root = tk.Tk()
root.title("Apricot Converter")
mb = tk.Menu(root)

#File tab
fm = tk.Menu(mb, tearoff = 0)
fm.add_command(label = "Open", command = openFile)
fm.add_command(label = "Quit", command = leave)
mb.add_cascade(label = "File", menu = fm)

#Help tab
hm = tk.Menu(mb, tearoff = 0)
hm.add_command(label = "Help", command = showHelp)
mb.add_cascade(label = "Help", menu = hm)

root.config(menu = mb)

#Setting up the label
tk.Label(root, text = "Current file path:").pack()
filePath = tk.StringVar()
fplabel = tk.Label(root, textvariable = filePath)
fplabel.pack()

def conv():
    with open(fp, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")

        if not os.path.exists("Converted Csvs"):
            os.makedirs("Converted Csvs")

        for row in reader:
            cRow = [""] * 10 #Change this later
            #Transform the row with a giant if statement
            try: #Creates a separate file for each converted entry
                f = open(cRow[1] + cRow[0] + ".csv", "w+")
            except: #Adds a suffix if there's a duplicate file with the same name
                attempts = 1
                while attempts != 0:
                    try:
                        f = open("Converted Csvs/" + cRow[1] + cRow[0] + " (" + str(attempts) + ").csv", "w+")
                        attempts = 0
                    except:
                        attempts += 1
            with open(f, 'wb') as convfile:
                writer = csv.writer(convfile, delimiter = ",")
                writer.writerow(cRow)
                convfile.close()

        csvfile.close()

#Setting up the button
button = tk.Button(root, text = "Convert!", command = conv)
button.pack()

root.mainloop()