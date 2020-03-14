from tkinter import Entry
class CellTkinter(object):
    def __init__(self, root,row,column):
        self._root = root
        self._row = row
        self._column = column

    def _addEntry(self):
        self._value = ( Entry(self.nameFrame, width=5 ,textvariable = IntVar()) )
        self._value.grid( row= self._row , column=self._column ,padx = 0, pady=0, sticky = N+W+E)
    
    def getValue(self):
        return self._value

    def setValue(self, val):
        self._value.delete(0,END)
        self._value.insert(0,val)
        self._root.config(backgrount = "red")