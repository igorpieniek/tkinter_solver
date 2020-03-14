from tkinter import *

class CellTkinter(object):
    def __init__(self, root,row,column):
        self._root = root
        self._row = row
        self._column = column
        self._addEntry()

    def _addEntry(self):
        self._value = ( Entry(self._root, width=4 ,textvariable = IntVar()) )
        self._value.grid( row= self._row , column=self._column ,padx = 3, pady=3, sticky = N+W+E)
    
    def getValue(self):
        return self._value.get()

    def setValue(self, val): 
        if not self.getValue() : self._value.config(background = "red")
        self._value.delete(0,END)
        self._value.insert(0,str(val))
        