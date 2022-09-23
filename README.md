# Hardware Project Experience -- SAND-ART TABLE

## Project goal

Build a table similar to the "Sisyphus Magic Sand Coffee Table" that displays a sand art image via X-Y coordinates. An easy to use API should also be devoloped so images/text can be written in the sand. RGB leds should add additional ambience.

## Project Breakdown

### Mechanical/Physical

1. We need a table
2. We need a X-Y axis system like below -- COVERED
3. We need to think about the physical constraints of the table

The main component of the table is an X-Y axis system (like the 3 rail system below) 
![](./twoaxisrail.JPG)
![](./kriebels.JPG)

4. We may need to develop our own PCB to drive the stepmotors in an orderly fashion.


### Firmware prequisites

1. X-Y axis will have to be manipulated in a linear as well as a circular way. 
2. Letters & words could be written in the sand. Even better would be if this could be done with a touch screen (maybe this would be something for a future project).
3. The firmware should be able to take an image and draw the figure in the sand (or at least the crude outlines). 
4. RGB library for the ledstrips

This last bullet point presents its own problems. Is this done with fourier? Everything has to be drawn in a single line so I don't think this will be easy. 

Professors suggested we used CNC and GCODE to send commands to the drivers/stepmotors and treat the table as a "2D" 3D printer, cancelling out the Z-axis. 

We need to find a library to send and receive the GCODE commands. 

https://github.com/grbl/grbl is a library that will run on a vanilla Arduino, but we would have to refactor the code to make it work on a nucleo (OR WE COULD JUST USE AN ARDUINO IDK).

DEZE WERKT MET CPP MAAR GEEN DOCUMENTATIE
https://github.com/x893/CNC-STM32 


## Preliminary BOM

3 x rail system (geslepen as)       GOT IT
1 x ledstrips (ws2812 of ws281X)
2(3) x step motor                   GOT IT 
1 x microcontroller (stm32 type)    GOT IT  
3 x riemen                          GOT IT  
3 x tandwielen                      GOT IT  
1 x raspberry pi                    GOT IT  
1 x (strong) magnet     
1 x zand
1 x zeil
1 X tafel/glas/...

