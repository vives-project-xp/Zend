import numpy as np 
import serial
from sender import Sender
from functions import Functions

raspberry = Sender("AMA0")
testFunction = Functions()

raspberry.manual_command()

#raspberry.send_command("G0 X100 Y100")
#raspberry.send_command("G28")

#raspberry.draw_circle()

#raspberry.draw_one_circle()

#testFunction.testFigure()

#raspberry.parseFunction(testFunction.getX(), testFunction.getY())