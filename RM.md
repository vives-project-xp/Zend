# Hardware Project Experience -- SAND-ART TABLE

## Project goal

Build a table similar to the "Sisyphus Magic Sand Coffee Table" that displays a sand art image via X-Y coordinates. An easy to use API should also be devoloped so images/text can be written in the sand. RGB leds should add additional ambience.

## Project Breakdown

### Mechanical/Physical

1. We need a table
2. We need a X-Y axis system like below
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

## Preliminary BOM

3 x rail system (geslepen as)
1 x ledstrips (ws2812 of ws281X)
2(3) x step motor
1 x microcontroller (stm32 type)
3 x riemen
3 x tandwielen
1 x raspberry pi
1 x (strong) magnet
1 x zand
1 x zeil


## TODO 

eventueel ontwerpen van PCB van motordrivers
