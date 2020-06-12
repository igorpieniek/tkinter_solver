class Cell(object):
    def __init__(self, row, column):
        self._row = row
        self._column = column
        self._options = [x for x in range(1,10)]
        self._value =0
        self._calculateArea()

    def __eq__(self, value):
        return value._row == self._row and value._column == self._column

    def getRow(self): return self._row

    def getColumn(self): return self._column

    def delateOpt(self, number):
        if isinstance(number, list ):
            for i in number:
                try: self._options.remove(i)
                except: continue                
        elif isinstance(number, int ):
            try: self._options.remove(number)
            except: return

    def getNumOfOpt(self):return len(self._options)
    def getAreaRowMin(self): return self._areaRowMin
    def getAreaRowMax(self): return self._areaRowMax
    def getAreaColumnMin(self): return self._areaColumnMin
    def getAreaColumnMax(self): return self._areaColumnMax
    def getAreaNum(self): return self._areaNum

    def getValue(self):
        if len(self._options)==1:
            self._value =self._options[0]
            return self._value
        else:
            return self._value

    def getOptions(self): return self._options

    def _setBoundariesOfArea(self, rowMin, rowMax, columnMin, columnMax, areaNum):
            self._areaNum = areaNum
            self._areaRowMin = rowMin
            self._areaRowMax = rowMax
            self._areaColumnMin = columnMin
            self._areaColumnMax = columnMax

    def _calculateArea(self):
        if  self._row < 3 and self._column < 3 :
            self._setBoundariesOfArea(0,3,0,3,1)
        elif  self._row < 3 and self._column > 2 and self._column < 6 :
            self._setBoundariesOfArea(0,3,3,6,2)
        elif  self._row < 3 and self._column > 5 :
            self._setBoundariesOfArea(0,3,6,9,3)
        elif self._row > 2 and self._row < 6 and self._column < 3 :
            self._setBoundariesOfArea(3,6,0,3,4)
        elif  self._row > 2 and self._row < 6 and self._column > 2 and self._column < 6 :
            self._setBoundariesOfArea(3,6,3,6,5)
        elif  self._row > 2 and self._row < 6  and self._column > 5 :
            self._setBoundariesOfArea(3,6,6,9,6)

        elif  self._row > 5 and self._column < 3 :
            self._setBoundariesOfArea(6,9,0,3,7)
        elif  self._row > 5 and self._column > 2 and self._column < 6 :
            self._setBoundariesOfArea(6,9,3,6,8)
        elif  self._row > 5 and self._column > 5 :
            self._setBoundariesOfArea(6,9,6,9,9)

