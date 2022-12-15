import numpy as np
from scipy import signal #niet vergeten te installeren op rPi
import matplotlib.pyplot as plt


#This is where all the math for the figures happen. We added a bunch of functions like getradius etc
#that can be useful in the future for more complex figures

class Functions:
    def __init__(self):
        #first we create a bunch of arrays for the X and Y values of the different functions
        #some arrays are used for the linear others are used in the functions themselves,
        #but the final result will always be an array of STRINGS that are stored in 
        # self._x
        # self._y
        #these will be used by the Sender class.
        
        self._xFunction= []
        self._yFunction= []
        self._intX = []
        self._intY =[]
        self._x = []
        self._y = []
        self._n = np.linspace(0, 8*np.pi, 500)

        #Bunch of default values
        self.defaultOffsetX = 100
        self.defaultOffsetY = 100
        self.defaultOffsetMin = 0
        self.defaultOffsetMax = 200
        self.defaultRoundDown = 3
        self.defaultMultiplier = 5
        self.defaultGrowth = 1.2
        self.radius = 0
    
    
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


    def drawStar(self, amount, angle = 0, grow = 0):
        self.drawPolygon(amount, angle, grow)
        self.setRadius()

    def setRadius(self):
        self.radius = np.sqrt((self._intX[0][1] - self._intX[0][0])**2 + (self._intY[0][1] - self._intY[0][0])**2)

    def setRadius(self, startPointX, startPointY, endPointX, endPointY):
        self.radius = np.sqrt((endPointX - startPointX)**2 + (endPointY - startPointY)**2)

    def drawPolygon(self, amount, angle, grow):
        angle = (angle * np.pi / 180)
        if(grow != 1):
            growth = self.defaultGrowth*grow
        n = np.linspace(angle, 2*np.pi + angle, amount + 1)
        self._xFunction = [np.cos(n) * growth]
        self._yFunction = [np.sin(n) * growth]
        self.parser()

    def parser(self):
        x = np.around(self._xFunction, self.defaultRoundDown) * self.defaultMultiplier + self.defaultOffsetX
        y = np.around(self._yFunction, self.defaultRoundDown) * self.defaultMultiplier + self.defaultOffsetY
        self._intX = x[0].astype(int)
        self._intY = y[0].astype(int)
        self._x = self._intX.astype(str)
        self._y  = self._intY.astype(str)

    def clearFunction(self):                #voorlopig een rampfunctie
        y = signal.sawtooth(3*self._n)
        roundY = np.around(y, 3) * 10
        roundX = np.around(self._n, 3) * 10
        self._intX = roundX.astype(int)
        self._intY = roundY.astype(int)
        self._x = self._intX.astype(str)
        self._y = self._intY.astype(str)
    
    def plotFigure(self):
        plt.scatter(self._intX, self._intY)
        plt.show()

    def christmasTree(self):
        self._intX = [100, 130, 130, 175, 145, 160, 130, 145, 115, 130, 115, 100, 110, 110, 120, 105, 100, 95, 80, 90, 90, 100, 85, 70, 85, 55, 70, 40, 55, 25, 70, 70, 100]
        self._intY = [20, 20, 50, 50, 80, 80, 110, 110, 140, 140, 160, 130, 120, 150, 170, 180, 200, 180, 170, 150, 120, 130, 160, 140, 140, 110, 110, 80, 80, 50, 50, 20, 20]
        for item in self._intX:
            self._x.append(str(item))
        for item in self._intY:
            self._y.append(str(item))

    def drawPointedStar(self, amount = 6, angle = 90, grow = 10, innerGrow = 0):
        angle = (angle * np.pi / 180)
        amount = 2
        if amount <= 3:
            amount = 3
        growth = 1
        if grow != 0 or innerGrow > grow:
            growth = (self.defaultGrowth - 1)*grow +1
        innerGrowth = 1/2
        if innerGrow != 0 or innerGrow <= grow:
            innerGrowth = (self.defaultGrowth - 1)*grow +1
        n = np.linspace(angle, 2*np.pi + angle, amount + 1)
        self._xFunction = [np.cos(n) * growth]
        self._yFunction = [np.sin(n) * growth]
        for x in range(1, amount, 2):
            self._xFunction[0][x] = self._xFunction[0][x] * innerGrowth
            self._yFunction[0][x] = self._yFunction[0][x] * innerGrowth
        self.parser()

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
