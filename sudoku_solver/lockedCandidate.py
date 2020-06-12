from TechniquesTools import *
import copy
from Cell import *

class LockedCandidate(TechniquesTools):
    """description of class"""
    def __init__(self, array):
        self.array = array

    def process(self, cells, array ):
        self.foundStatus = False
        self.array = array
        self.cells = cells
        status = True
        while status:
            for index, oneCell in  enumerate(self.cells):
                self.__updateRow(oneCell)
                if not oneCell.getValue() : self.__updateColumn(oneCell)
                if not oneCell.getValue() : self.__update3x3Area(oneCell)
                status, indexToDel = self.updateOneOption(oneCell,len(self.cells), index)
                if indexToDel:
                        self.foundStatus = True
                        self.printSolvedCell(oneCell)
                        self.cells.pop(indexToDel)
                        break
            if not self.cells: status= False
        print(self.__class__.__name__, ' method stop working')
        return self.array, self.foundStatus
    
    def __updateRow(self, oneCell): return self.__update(oneCell, 'row')

    def __updateColumn(self, oneCell): return self.__update(oneCell, 'column')

    def __update3x3Area(self,oneCell): return self.__update(oneCell, 'Area')

    def __update(self, oneCell, rc):
        methods = {'row': Cell.getRow, 'column': Cell.getColumn, 'Area': Cell.getAreaNum}
        if rc in methods.keys():
            line = [cell for cell in self.cells if methods[rc](cell) == methods[rc](oneCell) and cell != oneCell]            
        else: raise Exception('no such dimension')
        return self.__checkLine(line,oneCell)


    def __checkLine(self, line, oneCell):
        deletedOptions = []
        options = oneCell.getOptions()
        toDeleteOptions = []
        for el in line:
            for val in el.getOptions():
                try: 
                    options.remove(val)
                    toDeleteOptions.append(val)
                except: continue              
        if len(options) == 1: 
            oneCell.delateOpt(toDeleteOptions)
        return oneCell