import time
import serial

class Sender:

    #BAUD RATE FOR ARDUINO MEGA IS 250000

    def __init__(self, port):
        self.__port = "/dev/tty" + str(port)
        self.__ser = serial.Serial(self.__port, 9600, timeout = 1)
        self.__response = ""
        if self.__ser.isOpen():
            print("everything ok") 
    
    #below 
        
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
                    message = input("Enter command")
                    self.__ser.write(message.encode())
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
