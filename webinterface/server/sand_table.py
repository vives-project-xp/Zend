import numpy as np 
import serial
from sender import Sender
from functions import Functions
import time

#program for running the app in console and configuring the grbl library
#just run with "python sand_table.py"

raspberry = Sender("ACM0")
testFunction = Functions()

raspberry.initializeTable()
raspberry.manual_command()
