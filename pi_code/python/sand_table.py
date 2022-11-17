import numpy as np 
import serial
from sender import Sender
from functions import Functions

#raspberry = Sender("AMA0")
arduino = Sender("COM8")
testFunction = Functions()

#raspberry.manual_command()
arduino.manual_command()

#raspberry.send_command("G0 X100 Y100")
#raspberry.send_command("G28")

#raspberry.draw_circle()

#raspberry.draw_one_circle()

#testFunction.clearFunction()
#testFunction.spiral()
#testFunction.plotFigure()
#print(testFunction.getX(), testFunction.getY()) 
#print("# X array = " + str(len(testFunction.getX())) + "# Y array = " + str(len(testFunction.getY())))

#raspberry.parseFunction(testFunction.getX(), testFunction.getY())