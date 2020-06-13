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
            if self._cells: self._array,foundStatus2 = self.__lockedCandidate.process(self._cells, self._array)
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

 
            
    def __str__(self):
        out = ''
        for row in self._array:
            out += str(row)+ '\n'
        return out