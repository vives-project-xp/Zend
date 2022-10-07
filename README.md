# Hardware Project Experience -- SAND-ART TABLE

## Project goal

Build a table similar to the "Sisyphus Magic Sand Coffee Table" that displays a sand art image via X-Y coordinates. An easy to use API should also be devoloped so images/text can be written in the sand. RGB leds should add additional ambience.

## Project Breakdown

### Mechanical/Physical

1. We need a table
2. We need a X-Y axis system like below -- COVERED
3. We need to think about the physical constraints of the table (really need to figure this out)

**update 06/10/2022**
The XY system we will take from a 3D printer, and simply remove the nozzle and the Z-axis stepmotor. There are mechanical detectors to limit the movement of the stepmotors, but we've encountered some weird behaviour where they would still try to move past the boundaries. 

The system is currently quite loud... maybe there's a way to make it quieter? 

We've also received a PCB with drivers for the stepmotors, that we will have to hook up to an Arduino (cfr firmware). The connectors didn't match, so the wiring needs to be adjusted accordingly. 


### Firmware prequisites

1. X-Y axis will have to be manipulated in a linear as well as a circular way.
2. Letters & words could be written in the sand. Even better would be if this could be done with a touch screen (maybe this would be something for a future project).
3. The firmware should be able to take an image and draw the figure in the sand (or at least the crude outlines). 
4. RGB library for the ledstrips

The third bullet point presents its own problems. Is this done with fourier? Everything has to be drawn in a single line  I don't think this will be easy. 

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

