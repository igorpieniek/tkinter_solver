from TechniquesTools import *
import copy

class LockedCandidate(TechniquesTools):
    """description of class"""
    def __init__(self, array):
        self.array = array

    def process(self, cells, array ):
        self.array = array
        self.cells = cells
        for index, oneCell in  enumerate(self.cells):
            pass

    def __checkLine(self, line, oneCell):      
        tempCells = copy.deepcopy(oneCell)
        for el in line:
            for val in el.getOptions():
                tempCells.delateOpt(val)
        if tempCells.getNumOfOpt() == 1: return tempCells.getValue()
        else: return None
    
    def __updateRow(self, oneCell): return self.__update(oneCell, 'row')

    def __updateColumn(self, oneCell): return self.__update(oneCell, 'column')


    def __update(self, oneCell, rc):
        if rc == 'row':
            row = oneCell.getRow()
            line = [cell for cell in self.cells if cell.getRow() == row and cell != oneCell]
        elif rc == 'column':
            column = oneCell.getColumn()
            line = [cell for cell in self.cells if cell.getColumn() == column and cell != oneCell]
        else: raise Exception('no such dimension')
        out = self.__checkLine(line,oneCell)
