class TechniquesTools():
    """description of class"""
    def printSolvedCell(self, cell):
        print('(' + str(cell.getRow()) 
                +', '+ str(cell.getColumn())
                + ') = ' + str(cell.getValue()) +' Method: '+self.__class__.__name__ )
    
    def updateOneOption(self, oneCell, lenCells, index):
        status = True
        indexToDel = None
        if oneCell.getNumOfOpt()==1:
            self.array[oneCell.getRow()][oneCell.getColumn()] = oneCell.getValue()
            indexToDel = index
        elif (index+1) == lenCells:
            #print(self.__class__.__name__,': Last cell without solving')
            status = False
        return status, indexToDel

    def resultOperations(self,indexToDel, oneCell,cells):
        if indexToDel: 
            self.foundStatus = True
            self.printSolvedCell(oneCell)
            cells.pop(indexToDel)
            #print(self.__class__.__name__, ' method stop working')
            return True
        return False