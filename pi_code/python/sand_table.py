import numpy as np 
import serial
from sender import Sender

raspberry = Sender("ACM0")

raspberry.manual_command()