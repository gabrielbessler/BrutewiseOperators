from tkinter import *
from tkinter.ttk import *
import BruteWise as BT
import threading
import winsound

def findResults():
    exportResults = exportChoice.get()
    print(exportResults)
    BT.SetExport(exportResults)
    BT.SetOperatorList(setDisplay.cget("text"))
    t = threading.Thread(target=BT.Main)
    t.daemon = True
    t.start()

def updateProgressBar():
    try:
        currProgress = BT.GetProgress()
    except:
        currProgress = 0
    progress.set(currProgress*100) #from 0 to 100
    root.after(1000, updateProgressBar)
    currentStepText.config(text = "%.2f" % (currProgress * 100) + "%")

def setSetOne():
    setVal = "['+','-', '/', '*']"
    setDisplay.config(text = setVal)

def setSetTwo():
    setVal = "['+', '-', '/', '*', '|', '&', '%']"
    setDisplay.config(text = setVal)

def setSetThree():
    setVal = "['&', '|', '+', '-', '*', '/', '%', '^', '<<', '>>', '//', '**', '+~']"
    setDisplay.config(text = setVal)

root = Tk()
root.title("BruteWise Operators")

root.resizable(width=False, height=False)

checkBox = IntVar()
progress = DoubleVar()
exportChoice = StringVar()

topFrame = Frame(root)
bottomFrame = Frame(root)
midFrame = Frame(root)
mid2Frame = Frame(root)

topFrame.pack(pady = 5)
midFrame.pack(pady = 20, padx = 10)
mid2Frame.pack()
bottomFrame.pack(side=BOTTOM)

setDisplay = Label(topFrame, text= "Choose a set", width=50, anchor=CENTER)
goButton = Button(topFrame, text="GO!", command=findResults)
setOneBtn = Button(midFrame, text="Set 1", command=setSetOne)
setTwoBtn = Button(midFrame, text="Set 2", command=setSetTwo)
setThreeBtn = Button(midFrame, text="Set 3", command=setSetThree)

csvBtn = Radiobutton(bottomFrame, text="Export as CSV", variable=exportChoice, value="CSV")
txtBtn = Radiobutton(bottomFrame, text="Export as TXT", variable=exportChoice, value="TXT")
noneBtn = Radiobutton(bottomFrame, text="Do not export", variable=exportChoice, value="NONE")

exportChoice.set("TXT")

currentStepNum = Label(mid2Frame, text="Step 1 -")
currentStepText = Label(mid2Frame, text="Waiting...")

goButton.pack(pady = 5, side=TOP)
setDisplay.pack(pady = 5)

setOneBtn.pack(side=LEFT)
setTwoBtn.pack(side=LEFT)
setThreeBtn.pack(side=LEFT)

progressbar = ttk.Progressbar(bottomFrame, orient=HORIZONTAL, length=200, variable=progress)
currentStepNum.pack(side=LEFT)
currentStepText.pack(side=RIGHT)
progressbar.pack(pady = 5)
txtBtn.pack()
csvBtn.pack()
noneBtn.pack()
progressbar.stop()
checkBox.set(1)
root.after(1000, updateProgressBar)
root.mainloop()
