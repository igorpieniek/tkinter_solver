class Cell(object):
    def __init__(self, row, column):
        self._row = row
        self._column = column
        self._options = [x for x in range(1,10)]
        self._value =0

    def getRow(self):
        return self._row

    def getColumn(self):
        return self._column

    def delateOpt(self, number):
        for i in range(len(number)):
            index =[k for k,e in enumerate(self._options) if e == number[i]]
            if index:
                self._options.remove(index)

    def getNumOfOpt(self):
        return len(self._options)

    def getValue(self):
        if len(self._options)==1:
            self._value =self._options[0]
            return self._value
        else:
            return self._value



