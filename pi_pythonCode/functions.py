import numpy as np
from scipy import signal #niet vergeten te installeren op rPi
import matplotlib.pyplot as plt



class Functions:
    def __init__(self):
        self._x = []
        self._y = []
        self._intX = []
        self._intY =[]
        self._n = np.linspace(0, 8*np.pi, 500)
    
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
        roundX = abs(np.around(x, 3) * 10)
        roundY = abs(np.around(y, 3) * 10)
        self._intX = roundX.astype(int)
        self._intY = roundY.astype(int)
        self._x = self._intX.astype(str)
        self._y = self._intY.astype(str)

    def clearFunction(self):                #voorlopig een rampfunctie
        y = signal.sawtooth(3*self._n)
        roundY = np.around(y, 3) * 10
        roundX = np.around(self._n, 3) * 10
        self._intX = roundX.astype(int)
        self._intY = roundY.astype(int)
        self._x = self._intX.astype(str)
        self._y = self._intY.astype(str)
    
    def drawPolygon(self, amount):
        n = np.linspace(0, 2*np.pi, amount + 1)
        self._xFunction = [np.cos(n)]
        self._yFunction = [np.sin(n)]
        self.parser()

    def plotFigure(self):
        plt.scatter(self._intX, self._intY)
        plt.show()

    def parser(self):
        x = np.around(self._xFunction, self.defaultRoundDown) * self.defaultMultiplier + self.defaultOffsetX
        y = np.around(self._yFunction, self.defaultRoundDown) * self.defaultMultiplier + self.defaultOffsetY
        self._intX = x.astype(int)
        self._intY = y.astype(int)
        self._strX = self._intX.astype(str)
        self._strY = self._intY.astype(str)
    
    def GetRadius(x1,x2,y1,y2):
        return np.sqrt((x2 - x1)**2+ (y2 - y1)**2)


    def getX(self):
        return self._x
    def getY(self):
        return self._y

    def getIntX(self):
        return self._intX
    def getIntY(self):
        return self._intY

