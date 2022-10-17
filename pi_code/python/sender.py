import time
import serial

class Sender:

    def __init__(self, port):
        self.__port = "/dev/tty" + str(port)
        self.__ser = serial.Serial(self.__port, 250000, timeout = 1)
        self.__response = ""
        if self.__ser.isOpen():
            print("everything ok") 
            self.__ser.write(("G28 \r \n").encode())  #defines feedrate to 1500 mm/min
            self.__ser.write(("M400 \r \n").encode())
    
    #below 

    def parseFunction(self, arrayX, arrayY):
        while True:
            if self.__ser.isOpen():
                for x, y in zip(arrayX, arrayY):
                    self.__ser.write(("G0 " +"X" + x + " Y" + y + " \r \n").encode())
                    #time.sleep(0.01)
                    #self.__ser.write(("M400 \r \n").encode())

                    print((" G0 " +"X" + x + " Y" + y + " \r \n"))
                    time.sleep(0.1)
                    response = self.__ser.readline()
                    print(response)
                    self.__ser.flushInput()
                    #self.__ser.write(("M400 \r \n").encode())





    def send_command(self, command):
        while len(self.__response) == 0: 
            if self.__ser.isOpen():
                print("Attempting to send stuff")
                time.sleep(1)
                self.__ser.write((command + " \r \n").encode())     #de \r (carriage return) en \n zijn nodig om naar de arduino mega te schrijven
                time.sleep(0.1)
                self.__response = self.__ser.readline()
                print(self.__response)
                self.__ser.flushInput()
                self.__ser.close()

    def manual_command(self):
        if self.__ser.isOpen():
            print("{} connected".format(self.__ser.port))
            time.sleep(1)
            try:
                while True:
                    message = input("Enter command: ")
                    self.__ser.write((message + "\r \n").encode())
                    time.sleep(0.1)
                    response = self.__ser.readline()
                    print(response)
                    self.__ser.flushInput()
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught")
                    
                    


    def draw_circle(self):
        while True:    
            if self.__ser.isOpen():
                print("Attempting to send stuff")
                time.sleep(1)
                self.__ser.write(("G2 I20 J20" + " \r \n").encode())
                time.sleep(0.1)
                self.__ser.write(("M400 \r \n").encode())
                self.__response = self.__ser.readline()
                print(self.__response)
                self.__ser.flushInput()

    def draw_one_circle(self):
            if self.__ser.isOpen():
                print("Attempting to send stuff")
                time.sleep(1)
                self.__ser.write(("G2 I20 J20" + " \r \n").encode())
                time.sleep(0.1)
                self.__ser.write(("M400 \r \n").encode())
                self.__response = self.__ser.readline()
                print(self.__response)
                self.__ser.flushInput()
