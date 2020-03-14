from Cell import *

class Solver(object):
    def __init__(self):
        self._cells = []

    def solve(self,array):
        self._copyArray(array)
        self._notSolvedArrayInit()
        self._firstMethod()

    def _copyArray(self,array):
        if len(array) != 9:
            error('Macierz ma za mało rzędów!')
        for i in range(len(array)):
            if len(array[i]) != 9:
                error('Macierz ma za mało kolumn w rzędzie:', i)
       
        self._array = array

    def _notSolvedArrayInit(self):
        self._notSolvedIndex = []
        for r in range(len(self._array)):
            for c in range(len(self._array[r])):
                if not self._array[r][c]:
                    self._cells.append(Cell(r,c))

    def _firstMethod(self):
        status = True      
        while status:
            indexToDel = []
            for index,cellNum in  enumerate(self._cells):
                # get in Row update 
                for colNum in range( len( self._array[cellNum.getColumn()] ) ):
                    if self._array[cellNum.getRow()][colNum]:
                        cellNum.delateOpt(self._array[cellNum.getRow()][colNum])

                # get in Column update 
                for rowNum in range( len( self._array[cellNum.getRow()] ) ):
                    if self._array[rowNum][cellNum.getColumn()]:
                        cellNum.delateOpt(self._array[rowNum][cellNum.getColumn()])
                    
                # get in 3x3 Area update        
                for rowNum in range(cellNum.getAreaRowMin(), cellNum.getAreaRowMax() ):
                    for colNum in  range(cellNum.getAreaColumnMin(), cellNum.getAreaColumnMax() ):
                        if self._array[rowNum][colNum]:
                            cellNum.delateOpt(self._array[rowNum][colNum])

                # check if only one oppurtunity
                if cellNum.getNumOfOpt() == 1:
                    print( 'P(' + str(cellNum.getRow()) 
                            +', '+ str(cellNum.getColumn())
                            + ' Val: '+ str(cellNum.getValue()) )
                    self._array[cellNum.getRow()][cellNum.getColumn()] = cellNum.getValue()
                    indexToDel.append(index)
                    break
                elif (index+1) == len(self._cells):

                    print('Last cell without solving')
                    self._printOptions()
                    status = False
                
            if indexToDel: self._cells.pop(indexToDel[-1])
            if not self._cells: status = False
        self._printArray()
    def _printOptions(self):
        for i in self._cells:
            print( 'P(' + str(i.getRow()) 
                +', '+ str(i.getColumn())
                + ') Opt:' + str(i.getOptions()) )

    def _printArray(self):
        print('Wynik :')
        for row in range(len(self._array[0])):
            print(self._array[row])             