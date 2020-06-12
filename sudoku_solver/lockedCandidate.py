from TechniquesTools import *
import copy
from Cell import *

class LockedCandidate(TechniquesTools):
    """Method of solving sudoku called locked candidate method"""
    def __init__(self, array):
        self.array = array

    def process(self, cells, array ):
        self.foundStatus = False
        self.array = array
        self.cells = copy.deepcopy(cells)
        
        for index, oneCell in  enumerate(cells):          
            self.__updateRow(oneCell)
            if not oneCell.getValue() : self.__updateColumn(oneCell)
            if not oneCell.getValue() : self.__update3x3Area(oneCell)
            status, indexToDel = self.updateOneOption(oneCell,len(cells), index)
            if not status: return self.array, False
            if indexToDel: break
        self.resultOperations(indexToDel, oneCell, cells)  
        return self.array, self.foundStatus
           

    def __updateRow(self, oneCell): self.__update(oneCell, 'row')

    def __updateColumn(self, oneCell): self.__update(oneCell, 'column')

    def __update3x3Area(self,oneCell): self.__update(oneCell, 'Area')

    def __update(self, oneCell, rc):
        methods = {'row': Cell.getRow, 'column': Cell.getColumn, 'Area': Cell.getAreaNum}
        if rc in methods.keys():
            line = [cell for cell in self.cells if methods[rc](cell) == methods[rc](oneCell) and not cell == oneCell]            
        else: raise Exception('no such dimension')
        self.__checkLine(line,oneCell)

    def __checkLine(self, line, oneCell):
        deletedOptions = []
        options = copy.copy(oneCell.getOptions())
        toDeleteOptions = []
        for el in line:
            for val in el.getOptions():
                try: 
                    options.remove(val)
                    toDeleteOptions.append(val)
                except: continue              
        if len(options) == 1: 
            oneCell.delateOpt(toDeleteOptions)
