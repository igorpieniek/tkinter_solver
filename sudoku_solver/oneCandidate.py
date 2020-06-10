from Cell import *
from TechniquesTools import *

class OneCandidate(TechniquesTools):
    """Method of solving sudoku called one candidate method"""
    def __init__(self, array):
        self.array = array

    def process(self, cells, array ):
        self.array = array #update in case any number was added in other method
        status = True
        while status:
            for index, oneCell in  enumerate(cells):
                self.__updateRow(oneCell)
                self.__updateColumn(oneCell)
                self.__update3x3Area(oneCell)
                status, indexToDel = self.__updateOneOption(oneCell,len(cells), index)
                if indexToDel:
                    TechniquesTools.printSolvedCell(self,cells[indexToDel])
                    cells.pop(indexToDel)
                    break
            if not cells: status= False
        print('OneCandidate method stop working')
        return self.array


    def __updateOneOption(self, oneCell, lenCells, index):
        status = True
        indexToDel = None
        if oneCell.getNumOfOpt()==1:
            self.array[oneCell.getRow()][oneCell.getColumn()] = oneCell.getValue()
            indexToDel = index
        elif (index+1) == lenCells:
            print('Last cell without solving')
            status = False
        return status, indexToDel

    def __update(self, oneCell, rc):
        if rc == 'row':
            line = oneCell.getRow()
            arrayPart= self.array[line]
        elif rc == 'column':
            line = oneCell.getColumn()
            arrayPart= [row[line] for row in self.array]
        else: raise Exception('No such dimension - accepted only row or column')
       
        for el in range( len( arrayPart ) ):
            if arrayPart[el]:
                oneCell.delateOpt(arrayPart[el])
        return oneCell

    def __updateRow(self, oneCell):
        return self.__update(oneCell, 'row')

    def __updateColumn(self, oneCell):
        return self.__update(oneCell, 'column')

    def __update3x3Area(self, oneCell):
        rmin, rmax = oneCell.getAreaRowMin(),  oneCell.getAreaRowMax()
        cmin, cmax = oneCell.getAreaColumnMin(),  oneCell.getAreaColumnMax()
        for row in range(rmin, rmax ):
            for col in  range(cmin, cmax ):
                if self.array[row][col]:
                    oneCell.delateOpt( self.array[row][col] )
        return oneCell
    
