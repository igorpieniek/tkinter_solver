from Solver import *
from tkinter import *
from CellTkinter import CellTkinter

root = Tk()
root.geometry('370x315')
solv = Solver()
array = []

def solve(array):
    return solv.solve(array)

def sendArray(array):
    #build multi dimension array
    arrToSend = []
    rows = []
    
    for c in range(len(array[0])):
        rows =[]
        for r in range(len(array[0])):
            rows.append(int(array[r][c].getValue()))
        arrToSend.append(rows)

    solved = []
    solved = solve(arrToSend)
     
    for c in range(len(array[0])):
        for r in range(len(array[0])):
            array[c][r].setValue(solved[r][c])

def clear():
    array = []
    for c in range(9):
        col = []
        for r in range(9):
            col.append(CellTkinter(entryFrame,r,c))        
        array.append(col)

buttonFrame = LabelFrame(root, padx = 5, pady=5,width =300)
buttonFrame .grid(row = 0,column = 0, stick = W+N+E)
entryFrame = LabelFrame(root, padx = 5, pady=5)
entryFrame .grid(row = 1,column = 0, stick = W+N+E)
button = Button(buttonFrame, text= "Solve",padx=0, pady=0, command = lambda:sendArray(array))
button.grid(row = 0,column = 0, stick = W+N+E)
buttonClear = Button(buttonFrame, text= "Clear",padx=0, pady=0, command = lambda:clear())
buttonClear.grid(row = 0,column = 1, stick = W+N+E)


for c in range(9):
    col = []
    for r in range(9):
        col.append(CellTkinter(entryFrame,r,c))        
    array.append(col)




root.mainloop()