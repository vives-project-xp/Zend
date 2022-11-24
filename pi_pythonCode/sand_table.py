import numpy as np 
import serial
from sender import Sender
from functions import Functions
import time


raspberry = Sender("ACM0")
testFunction = Functions()

#raspberry.send("G0 X10 Y10")

raspberry.initializeTable()
raspberry.manual_command()

#raspberry.draw_circle()

#raspberry.draw_one_circle()

#testFunction.clearFunction()

#print(testFunction.getX())
#print(testFunction.getY())

#testFunction.spiral()
#print(testFunction.getX())
#print(testFunction.getY())
#raspberry.parseFunction(testFunction.getX(), testFunction.getY())