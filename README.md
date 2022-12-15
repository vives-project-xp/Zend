# Hardware Project Experience -- SAND-ART TABLE

## Project goal

Build a table similar to the "Sisyphus Magic Sand Coffee Table" that displays a sand art image via X-Y coordinates. An easy to use API should also be devoloped so images/text can be written in the sand. RGB leds should add additional ambience.

## Project Breakdown

### Mechanical/Physical

We used a 3D printer (Ultimaker) and removed the Z-axis controls. A grbl shield attached to an arduino interfaces with the stepper motors. 
For the table itself we used a Lack table from Ikea. The sand itself is kept in a plexiglass tray. The ball is moved by magnets attached to the 3d printer and draws geometrical figures in the sand. 


**Dimensions**
width: 48cm x 34cm
height:xxx



### Firmware

To control the 3d printer we used the grbl library. (https://github.com/grbl/grbl)
This is an alternative to more complex firmware like Marlin and runs on a vanilla Arduino (or any other model as long as it sports an Atmega 328).

![gShield v5b](./img/gShield.jpg)

To control the stepper motors we use the gShield v5b which is compatible with an arduino uno.
To get the correct altered firmware on the arduino execute the following steps:
If you cloned this repo go to the 'grbl-library' folder, extract the grbl.zip to C:\Users\[you user]\Documents\Arduino\libraries
Now open Arduino IDE (some newer versions of the IDE may cause trouble to execute the next steps, if trouble occurs I recommend using Arduino IDE 1.8.19)
Go to sketch->Include Library->Add .ZIP library... Now go to documents->Arduino->libraries and select the grbl folder, hit open.
To upload the file go to File->Examples->grbl->grblUpload.
Now you can compile and upload the file.

The grbl library is configured through serial communication, so the first step was to write a small program that writes and

Professors suggested we used CNC and GCODE to send commands to the drivers/stepmotors and treat the table as a "2D" 3D printer, cancelling out the Z-axis. 

We need to find a library to send and receive the GCODE commands. 

**update 06/10/2022** 

---- LED STRIPS ----
We managed to get the LED-strips working with the WLED library. Next step is to build an interface with the raspberry pi and trigger them when the drawing process begins. 

---- FIRMWARE ----
Serial communication between the raspberry pi and the arduino has been fixed. Right now we can send GCODE both with python and with C++. 

I'm still not sure what language we should use for the serial communication. The advantage of python is that we can handle the figures in numpy. The advantage of cpp is that it's cpp. 


https://github.com/grbl/grbl is a library that will run on a vanilla Arduino.

DEZE WERKT MET CPP MAAR GEEN DOCUMENTATIE
https://github.com/x893/CNC-STM32 




## Preliminary BOM

3 x rail system (geslepen as)       GOT IT
1 x ledstrips (ws2812 of ws281X)    GOT EM
2(3) x step motor                   GOT IT 
1 x microcontroller (stm32 type)    GOT IT  
3 x riemen                          GOT IT  
3 x tandwielen                      GOT IT  
1 x raspberry pi                    GOT IT  
1 x (strong) magnet     
1 x zand
1 x zeil
1 X tafel/glas/...


## Ideas for future implementations

1. Letters & words could be written in the sand. Even better would be if this could be done with a touch screen (maybe this would be something for a future project).
2. The firmware should be able to take an image and draw the figure in the sand (or at least the crude outlines). 