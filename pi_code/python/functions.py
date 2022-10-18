import numpy as np
import matplotlib.pyplot as plt



class Functions:
    def __init__(self):
        self._x = []
        self._y = []
        self._intX = []
        self._intY =[]
        self._n = np.linspace(0, 8*np.pi, 100)
    
    def testFigure(self):
        x = np.sin(self._n)**3
        y = np.cos(self._n)**3
        roundX = np.around(x, 3) *100
        roundY = np.around(y, 3) * 100
        self._intX = roundX.astype(int)
        self._intY = roundY.astype(int)
        self._x = self._intX.astype(str)
        self._y = self._intY.astype(str)
        
    def spiral(self):
        x = self._n*(np.cos(self._n))
        y = self._n*(np.sin(self._n))
        tempX = np.around(x, 3) * 10
        tempY = np.around(y, 3) * 10
        self._intX = tempX.astype(int)
        self._intY = tempY.astype(int)
        self._x = self._intX.astype(str)
        self._y = self._intY.astype(str)

    def clearFunction(self):
        return 0

    def plotFigure(self):
        plt.scatter(self._intX, self._intY)
        plt.show()


    def getX(self):
        return self._x
    def getY(self):
        return self._y

