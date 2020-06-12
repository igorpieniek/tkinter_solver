from Cell import *
import copy
from oneCandidate import *
from lockedCandidate import *

class Solver(object):
    def __init__(self):
        self._cells = []

    def solve(self,array):
        self._copyArray(array)
        self._notSolvedArrayInit()
        self.__oneCandidate = OneCandidate(array)
        self.__lockedCandidate = LockedCandidate(array)
        status = True
        while status:
            self._array, foundStatus1 = self.__oneCandidate.process(self._cells, self._array)
            if self._cells: 
                #foundStatus2= self._secondMethod()
                self._array,foundStatus2 = self.__lockedCandidate.process(self._cells, self._array)
                
            else : break
        
            if not (foundStatus1 or foundStatus2): break


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


    def _secondMethod(self):
        #self._array = self.__lockedCandidate.process(self._cells, self._array)
        status = True      
        while status:
            indexToDel = []
            for index,cellNum in  enumerate(self._cells):
                #copy options

                print(cellNum.getRow(), cellNum.getColumn())
                options = cellNum.getOptions()              
                
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
                    if (c.getAreaNum() == cellNum.getAreaNum() and 
                       c !=cellNum):
                            sameArea.append(c)
                toDel = []
                fullstatus = True
                opt = copy.deepcopy(cellNum)
                # get in Row update 
                for row in sameRow:
                    for val in row.getOptions():
                        opt.delateOpt(val)
                        toDel.append(val)
                if opt.getNumOfOpt() == 1: fullstatus = False

                # get in Column update
                if fullstatus:
                    del opt
                    toDel = []
                    opt = copy.deepcopy(cellNum)
                    for col in sameColumn:
                        for val in col.getOptions():
                            opt.delateOpt(val)
                            toDel.append(val)
                    if opt.getNumOfOpt() == 1: fullstatus = False
                # get in Area update
                if fullstatus:
                    del opt
                    toDel = []
                    opt = copy.deepcopy(cellNum)
                    for area in sameArea:
                        for val in area.getOptions():
                            opt.delateOpt(val)
                            toDel.append(val)
                
                print('options ', options, ' toDel ', list(set(toDel)))
                # check if only one oppurtunity
                if opt.getNumOfOpt() == 1:
                    print( 'P(' + str(opt.getRow()) 
                            +', '+ str(opt.getColumn())
                            + ') Val: '+ str(opt.getValue()) + ' Second' )
                    self._array[cellNum.getRow()][cellNum.getColumn()] = opt.getValue()
                    indexToDel = index
                    break
                elif (index+1) == len(self._cells):

                    print('METHOD 2 : END OF IDEAS')
                    if False : self._printOptions()
                    return False
                    status = False


            if indexToDel:
               self._cells.pop(indexToDel)
               return True
            else: return False
            #if not self._cells: return False


    def _printOptions(self):
        for i in self._cells:
            print( 'P(' + str(i.getRow()) 
                +', '+ str(i.getColumn())
                + ') Opt:' + str(i.getOptions()) )

    def _printArray(self):
        print('Wynik :')
        for row in range(len(self._array[0])):
            print(self._array[row])  
            
    def __str__(self):
        out = ''
        for row in self._array:
            out += str(row)+ '\n'
        return out