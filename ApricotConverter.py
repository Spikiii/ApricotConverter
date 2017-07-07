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
    if(fp != ""):
        with open(fp, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter = ",")

            if not os.path.exists(fp + "/../Converted Csvs"):
                os.makedirs(fp + "/../Converted Csvs")

            for row in reader:
                cRow = [""] * 77 #Change this later

                #Clients.csv
                commaPos = row[0].index(",")
                cRow[2] = row[0][:commaPos]  #Last name
                firstPos = len(cRow[2]) + 2
                middlePos = row[0][firstPos:].index(" ") + firstPos
                cRow[0] = row[0][firstPos:middlePos] #First name
                cRow[1] = row[0][middlePos + 1:] #Middle name
                cRow[3] = row[12] #Application date
                cRow[6] = row[6] #DOB
                cRow[15] = row[1] #Address, line 1
                try:
                    commaPos = row[1].index(",")
                    cRow[16] = row[1][commaPos + 1:] #Address, line 2
                except:
                    cRow[16] = ""
                cRow[18] = row[2] #City
                cRow[19] = "Il"
                cRow[21] = row[3] #Zip code
                cRow[22] = "United States"
                cRow[25] = row[13] #Ward
                cRow[27] = row[4] #Phone number
                cRow[29] = row[5] #Email

                #LongTermCareCaseNotes.csv
                cRow[64] = cRow[0] #First Name
                cRow[65] = cRow[1] #Middle Name
                cRow[66] = cRow[2] #Last Name

                #ProgramEnrollment.csv
                cRow[71] = cRow[0]
                cRow[72] = cRow[1]
                cRow[73] = cRow[2]
                cRow[74] = row[9] #Program enrollment
                cRow[75] = row[11] #Start date
                cRow[76] = row[12] #End date

                fPath = fp + '/../Converted Csvs/' + cRow[2].lower() + cRow[0][0].upper() + cRow[0][1:].lower() + '.csv'
                if(os.path.isfile(fPath)): #Checks for duplicate files, and makes new files
                    attempts = 1
                    fPath = fPath[:len(fPath) - 4]
                    fPath += " (" + str(attempts) + ").csv"
                    prevLen = len(" (" + str(attempts) + ").csv")
                    while(os.path.isfile(fPath)):
                        attempts += 1
                        fPath = fPath[:len(fPath) - prevLen]
                        fPath += " (" + str(attempts) + ").csv"
                        prevLen = len(" (" + str(attempts) + ").csv")
                f = open(fPath, 'w')
                f.close()
                with open(fPath, 'wt') as convfile:
                    writer = csv.writer(convfile, delimiter=",")
                    writer.writerow(cRow)
                    convfile.close()
                print("Wrote " + fPath[:22] + fPath[61:])
            csvfile.close()

#Setting up the button
button = tk.Button(root, text = "Convert!", command = conv)
button.pack()

root.mainloop()