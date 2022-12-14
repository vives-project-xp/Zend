import time
import serial
#SWITCH BETWEEN THESE TWO IMPORTS FOR WEBFUNCTIONALITY OR CONSOLE DEBUGGING WITH SAND_TABLE.PY
from .functions import Functions
#from functions import Functions
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)   
GPIO.setup(24, GPIO.OUT)

#THIS IS THE CLASS THAT INTERFACES BETWEEN THE RASPBERRY PI AND THE ARDUINO

class Sender:

    #FIRST DEFINE THE COM PORT, BAUD RATE AND TIMEOUT. PRINT AN OK IF IT WORKS OR NOT
    #BAUD RATE FOR VANILLA ARDUINO IS 115200
    def __init__(self, port):
        self.__port = "/dev/tty" + str(port)
        self.__ser = serial.Serial(self.__port, 115200, timeout = 1)
        self.__feedRate = 1000
        self.__trigger = True
        if self.__ser.isOpen():
            print("everything ok")
            
        else:
            print("Not ok")
            

    #function for initializing the table.
    def initializeTable(self):
        if self.__ser.isOpen():
            #wait 3 seconds and send the home command
            time.sleep(3)
            command = "$h\r\n"
            self.__ser.write(command.encode())
            #wait 1 second and set the feedrate for circular movements
            time.sleep(1)
            self.__ser.write(("F"+str(self.__feedRate)+ "\r\n").encode())

            #always flush the input for good measure
            self.__ser.flushInput()


    #function for sending a manual command. Has to be entered as a string 
    #e.g. message = "G0 X10 Y10"
    def send(self, message):
        command = f"{message}\r\n"
        print(command)
        if self.__ser.isOpen():
            time.sleep(1)
            self.__ser.write(command.encode())
            response = self.__ser.readlines()
            for value in response:
                print(value.decode('utf-8'))
            self.__ser.flushInput()

    #hardreset function. 
    def hardReset(self):
        if self.__ser.isOpen():
            GPIO.output(24,0)
            time.sleep(1)
            GPIO.output(24,1)
            self.initializeTable()
    
#THIS IS THE "MAIN" FUNCTION FOR DEBUG USE WITH SAND_TABLE.PY. YOU CAN ENTER MANUAL COMMANDS OR TRY SOME FIGURES
#BY TYPING "kerst" OR "parse" OR "star"                
    def manual_command(self):
        try:

            if self.__ser.isOpen():
                print("{} connected".format(self.__ser.port))           
                time.sleep(1)
                while True:
                        message = input("Enter command: ")
                        if(message == "test"):
                            self.drawSpiral()
                        elif(message == "send"):
                            self.send("G0 X50 Y10")
                        elif(message == "star"):
                            self.drawStar()
                        elif(message == 'kerst'):
                            self.drawTree()
                        elif(message == "parse"):
                            testFunction = Functions()
                            testFunction.clearFunction()
                            self.parseLinFunction(testFunction.getX(), testFunction.getY())
                        elif(message == "poly"):
                            self.drawPolygon()
                        elif(message == "pointy"):
                            self.drawPointyStar()
                        elif(message == "stop"):
                            self.hardReset()
                        
                        self.__ser.write((message + "\r\n").encode())
                        time.sleep(0.1)
                        response = self.__ser.readlines()
                        for values in response:
                            print(values.decode('utf-8'))
                        self.__ser.flushInput()
        except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught")
                    
                      
    
    #function for drawing 2 mirrored "spirals" 
    def drawSpiral(self):
        i = 1
        self.send("G0 X100 Y100")
        time.sleep(3)
        
        while i < 5 or self.__trigger == True:
            time.sleep(1)
            self.send("G2 X100 Y100 I"+str(i * 10))
            i += 1
            if i == 5:
                i = i * -1

    #function for drawing a polygon
    def drawPolygon(self):
        poly = Functions()
        amount = 0
        while amount <= 10 or self.__trigger == True:
            poly.drawPolygon(amount, 54, 14)
            self.parseLinFunction(poly.getX(), poly.getY())
            amount += 1
            if amount == 9:
                amount = 0
    
    #function for drawing a pointystar
    def drawPointyStar(self):
        star = Functions()
        amount = 0
        while amount <= 10:
            star.drawPointedStar(amount, 90)
            self.parseLinFunction(star.getX(), star.getY())
            amount += 1
            if amount == 9:
                amount = 0



    #function for drawing a christmas tree
    def drawTree(self):
        tree = Functions()
        tree.christmasTree()
        self.parseLinFunction(tree.getX(), tree.getY())
    
    # function for drawing a 4 pointed curved star that changes
    # angle. Hardcoded and bloated for test purposes.
    def drawStar(self):
        x = 0 
        y = 0 
        i = 0
        try:   
            while True or self.__trigger ==  True: 
                self.send("G3 X" + str(x) +" Y" + str(100 + y)+ " R100")
                time.sleep(4)
                self.send("G3 X" + str(100 + x) + " Y" + str(200 - y) + " R100")
                time.sleep(4)
                self.send("G3 X" + str(200-x) + " Y" + str(100 - y) + " R100")
                time.sleep(4)
                self.send("G3 X"+ str(100-x) + " Y" + str(y) + " R100")
                time.sleep(4)
                x += 20
                y += 20
                i += 1
                if i == 7:
                    x = 0
                    y = 0
                    i = 0
        except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught")

    # this function can be used to parse a more complex function (see function class)
    # in a circular motion.
    def parseCircularFunction(self, arrayX, arrayY):
        i = 0.1
        if self.__ser.isOpen():
            for x, y in zip(arrayX, arrayY):
                time.sleep(0.1)                
                self.send("G3 " +"X" + x + " Y" + y + " R" + str(i))
                response = self.__ser.readlines()
                print(response)
                self.__ser.flushInput()

    #this function can be used to parse a more complex figure in a linear motion
    #for example the christmas tree
    def parseLinFunction(self, arrayX, arrayY):
            if self.__ser.isOpen():
                for x, y in zip(arrayX, arrayY):
                    time.sleep(0.1)
                    self.send(" G0 X" + x + " Y" + y)
                    response = self.__ser.readlines()
                    print(response)
                    self.__ser.flushInput()
