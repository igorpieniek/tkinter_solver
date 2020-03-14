
class Solver(object):
    def __init__(self):
        pass

    def solve(self,array):
        self._copyArray(array)
        self._notSolvedArrayInit()

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
                    self._notSolvedIndex.append([r,c])

    def _firstMethod(self):
        while True:
            #main loop to check rows
            status = True
            for pointToSolve in range(len( self._notSolvedIndex)):
                # row checking
                used =[]
                for col in range(len(self._array[pointToSolve[0]])):
                    if self._array[pointToSolve[0]][col] :
                        used.append(col)
                    

