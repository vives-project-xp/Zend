import numpy as np 
import serial
from .sender import Sender
from .functions import Functions
import time

#program for running the app in console and configuring the grbl library

raspberry = Sender("ACM0")
testFunction = Functions()

#raspberry.send("G0 X10 Y10")

raspberry.initializeTable()
raspberry.manual_command()
