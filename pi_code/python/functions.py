import numpy as np



class Functions:
    def __init__(self):
        self._x = []
        self._y = []
        self._n = np.linspace(0, 2*np.pi, 100)
    
    def testFigure(self):
        tempX = np.sin(self._n)**3
        tempY = np.cos(self._n)**3
        roundX = np.around(tempX, 4) *100
        roundY = np.around(tempY, 4) * 100
        intX = roundX.astype(int)
        intY = roundY.astype(int)
        self._x = intX.astype(str)
        self._y = intY.astype(str)


    def getX(self):
        return self._x
    def getY(self):
        return self._y



