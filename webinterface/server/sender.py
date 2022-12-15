import time
import serial
from functions import Functions
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)   
GPIO.setup(24, GPIO.OUT)


class Sender:

    #BAUD RATE FOR ARDUINO MEGA IS 250000

    def __init__(self, port):
        self.__port = "/dev/tty" + str(port)
        self.__ser = serial.Serial(self.__port, 115200, timeout = 1)
        self.__i = 3
        if self.__ser.isOpen():
            print("everything ok")
            
        else:
            print("Not ok")
            


    def initializeTable(self):
        if self.__ser.isOpen():
            time.sleep(3)
            command = "$h\r\n"
            self.__ser.write(command.encode())
            time.sleep(1)
            self.__ser.write(("F1000 \r\n").encode())
            self.__ser.flushInput()

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


    def hardReset(self):
        if self.__ser.isOpen():
            self.send("$X")
            time.sleep(1)
            GPIO.output(24,0)
            time.sleep(1)
            GPIO.output(24,1)
            time.sleep(1)
            self.send("G0 X-20")
            time.sleep(1)
            self.initializeTable()
            
                    
    def manual_command(self):
        try:

            if self.__ser.isOpen():
                print("{} connected".format(self.__ser.port))           
                time.sleep(1)
                while True:
                        message = input("Enter command: ")
                        if(message == "test"):
                            self.testSpiral()
                        elif(message == "send"):
                            self.send("G0 X50 Y10")
                        elif(message == "star"):
                            self.drawStar()
                        elif(message == 'kerst'):
                            kerstboom = Functions()
                            kerstboom.cristmasTree()
                            self.parseLinFunction(kerstboom.getX(), kerstboom.getY())
                        elif(message == "parse"):
                            testFunction = Functions()
                            testFunction.clearFunction()
                            self.parseLinFunction(testFunction.getX(), testFunction.getY())
                        elif(message == "poly"):
                            self.drawPolygon()
                        elif(message == "hardreset"):
                            self.hardReset()

                        self.__ser.write((message + "\r\n").encode())
                        time.sleep(0.1)
                        response = self.__ser.readlines()
                        for values in response:
                            print(values.decode('utf-8'))
                        self.__ser.flushInput()
        except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught")
                    
                    

    def testSpiral(self):
        i = 1
        self.send("G0 X100 Y100")
        time.sleep(3)
        
        while i < 5:
            time.sleep(1)
            self.send("G2 X100 Y100 I"+str(i * 10))
            i += 1
            if i == 5:
                i = i * -1

    def drawPolygon(self):
        poly = Functions()
        poly.drawPolygon(3, 54, 14)
        while True:
            # HIER BEN JE GEEINDIGD FIX DIE SHIT DE PARSELINFUNCTION ZAT OOK IN EEN WHILETRUE
            self.send("")

    




    def drawStar(self):
        x = 0
        y = 0
        i = 0
        try:   
            while True: 
                self.send("G3 X" + str(x) +" Y" + str(100 + y)+ " R100")
                time.sleep(3)
                self.send("G3 X" + str(100 + x) + " Y" + str(200 - y) + " R100")
                time.sleep(3)
                self.send("G3 X" + str(200-x) + " Y" + str(100 - y) + " R100")
                time.sleep(3)
                self.send("G3 X"+ str(100-x) + " Y" + str(y) + " R100")
                time.sleep(3)
                x += 20
                y += 20
                i += 1
                if i == 40:
                    x = 0
                    y = 0
                    i = 0
        except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught")

    def parseCircularFunction(self, arrayX, arrayY):
        while True:
            if self.__ser.isOpen():
                for x, y in zip(arrayX, arrayY):
                    time.sleep(0.1)
                    i += 0.1
                    self.__ser.write(("G3 " +"X" + x + " Y" + y + " I" + str(i) + "\r \n").encode())
                    response = self.__ser.readlines()
                    print(response)
                    self.__ser.flushInput()

    def parseLinFunction(self, arrayX, arrayY):
            if self.__ser.isOpen():
                for x, y in zip(arrayX, arrayY):
                    time.sleep(1)
                    self.send(" G0 X" + x + " Y" + y)
                    response = self.__ser.readlines()
                    print(response)
                    self.__ser.flushInput()
