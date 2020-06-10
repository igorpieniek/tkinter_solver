class TechniquesTools():
    """description of class"""
    def printSolvedCell(self, cell):
        print('(' + str(cell.getRow()) 
                +', '+ str(cell.getColumn())
                + ') = ' + str(cell.getValue()) +' Method: '+self.__class__.__name__ )
