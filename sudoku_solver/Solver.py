from Cell import *
import copy
from oneCandidate import *

class Solver(object):
    def __init__(self):
        self._cells = []

    def solve(self,array):
        self._copyArray(array)
        self._notSolvedArrayInit()
        self.__oneCandidate = OneCandidate(array)
        status = True
        while status:
            self._firstMethod()
            if self._cells: status= self._secondMethod()
            else : break

        return self._array

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

        self.__oneCandidate.process(self._cells, self._array)
        #status = True      
        #while status:
        #    indexToDel = []
        #    for index,cellNum in  enumerate(self._cells):
        #        # get in Row update 
        #        for colNum in range( len( self._array[cellNum.getColumn()] ) ):
        #            if self._array[cellNum.getRow()][colNum]:
        #                cellNum.delateOpt(self._array[cellNum.getRow()][colNum])

        #        # get in Column update 
        #        for rowNum in range( len( self._array[cellNum.getRow()] ) ):
        #            if self._array[rowNum][cellNum.getColumn()]:
        #                cellNum.delateOpt(self._array[rowNum][cellNum.getColumn()])
                    
        #        # get in 3x3 Area update        
        #        for rowNum in range(cellNum.getAreaRowMin(), cellNum.getAreaRowMax() ):
        #            for colNum in  range(cellNum.getAreaColumnMin(), cellNum.getAreaColumnMax() ):
        #                if self._array[rowNum][colNum]:
        #                    cellNum.delateOpt(self._array[rowNum][colNum])

        #        # check if only one oppurtunity
        #        if cellNum.getNumOfOpt() == 1:
        #            print( 'P(' + str(cellNum.getRow()) 
        #                    +', '+ str(cellNum.getColumn())
        #                    + ') Val: '+ str(cellNum.getValue()) + ' F')
        #            self._array[cellNum.getRow()][cellNum.getColumn()] = cellNum.getValue()
        #            indexToDel.append(index)
        #            break
        #        elif (index+1) == len(self._cells):

        #            print('Last cell without solving')
        #            if False :self._printOptions()
        #            status = False
                
        #    if indexToDel: self._cells.pop(indexToDel[-1])
        #    if not self._cells: status = False



    def _secondMethod(self):
        status = True      
        while status:
            indexToDel = []
            for index,cellNum in  enumerate(self._cells):
                #copy options

                #same row cells
                sameRow = []
                for c in self._cells:
                    if c.getRow() == cellNum.getRow() and c !=cellNum: sameRow.append(c)
                #same columns cells
                sameColumn = []
                for c in self._cells:
                    if c.getColumn() == cellNum.getColumn()and c !=cellNum: sameColumn.append(c)
                #same 3x3 Area cells
                sameArea = []
                for c in self._cells:
                    if (c.getAreaRowMin() == cellNum.getAreaRowMin() and
                       c.getAreaRowMax() == cellNum.getAreaRowMax() and
                       c.getAreaColumnMin() == cellNum.getAreaColumnMin() and
                       c.getAreaColumnMax() == cellNum.getAreaColumnMax() and 
                       c !=cellNum):
                            sameArea.append(c)

                fullstatus = True
                opt = copy.deepcopy(cellNum)
                # get in Row update 
                for row in sameRow:
                    for val in row.getOptions():
                        opt.delateOpt(val)
                if opt.getNumOfOpt() == 1: fullstatus = False

                # get in Column update
                if fullstatus:
                    del opt
                    opt = copy.deepcopy(cellNum)
                    for col in sameColumn:
                        for val in col.getOptions():
                            opt.delateOpt(val)
                    if opt.getNumOfOpt() == 1: fullstatus = False
                # get in Area update
                if fullstatus:
                    del opt
                    opt = copy.deepcopy(cellNum)
                    for area in sameArea:
                        for val in area.getOptions():
                            opt.delateOpt(val)

                # check if only one oppurtunity
                if opt.getNumOfOpt() == 1:
                    print( 'P(' + str(opt.getRow()) 
                            +', '+ str(opt.getColumn())
                            + ') Val: '+ str(opt.getValue()) + ' Second' )
                    self._array[cellNum.getRow()][cellNum.getColumn()] = opt.getValue()
                    indexToDel.append(index)
                    break
                elif (index+1) == len(self._cells):

                    print('METHOD 2 : END OF IDEAS')
                    if False : self._printOptions()
                    return False
                    status = False


            if indexToDel:
               self._cells.pop(indexToDel[-1])
               return True
            if not self._cells: return False


    def _printOptions(self):
        for i in self._cells:
            print( 'P(' + str(i.getRow()) 
                +', '+ str(i.getColumn())
                + ') Opt:' + str(i.getOptions()) )

    def _printArray(self):
        print('Wynik :')
        for row in range(len(self._array[0])):
            print(self._array[row])             