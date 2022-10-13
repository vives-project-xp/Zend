# LED STRIP DRIVER

## Intro

This directory is responsible for the initialization and control of the LED-strip which will be integrated in the Sand Table.
The LED-strip is programmed in Python. When creating the class and functionalities, [Python version 3.9.5](https://www.python.org/downloads/) works for this code.
The led-strip is connected to an [ESP8266](https://en.wikipedia.org/wiki/ESP8266) so that it can be connected to the internet. Then we can send all kinds of GET requests to the WLED API to change the behavior of the LED-strip. Different types of parameters that are added in the URL for the GET request can change the behavior of the LED-strip. An overview of all changeable elements of the LED-strip can be found [here](https://kno.wled.ge/interfaces/http-api/)

## Functions

There are a number of functions included in the [src/led.py](./src/led.py).

### Constructor

When a new object of the LedStrip class is created, one only needs to give the URL of the LED-strip and how many LEDs are on this strip. These parameters are saved as attributes and then used to send the first GET request. Additionally the brightness and effect index are created as a variable and set to a default value so that it can be initialized correctly. GET requests are sent via the python module: 'requests', imported at the beginning of the class file.
A few variables are created and set to a default value and then included in the final version of the URL to which the GET request will be sent.

### Setters

* setLedCount(number_of_leds)
This function can be called when the number of LEDs on the strip has to be updated. The number of LEDs will be saved in the attributes of the class and then a new get request will be sent to the ESP8266 to update the count.

* setPrimaryColor(hex_color) & setSecondaryColor(hex_color) & setThirdColor(hex_color)
These functions are used to change the primary, second and third color of the LED-strip. The user needs to enter a hex value (without any prefix, just 6 characters to represent the 3 RGB values) and then a GET request will be sent to update the color. The brightness is also sent each time as an extra security that the brightness would not change when updating the colors. The brightness is acquired via the brightness getter.

* setEffect(effect_index)
To change the effect on the LED-strip the effect index needs to be updated. A full list of all effects and their indices can be found [here](https://github.com/Aircoookie/WLED/wiki/List-of-effects-and-palettes). The user only needs to give an index number when calling the function. There is a security check to make sure that no number above 73 or under 0 is entered (the lowest and highest possible index). The effect index will be saved in its variable and a GET request will be sent to the LED-strip to change the effect.

* setBrightness(brightness)
Same concept as the setEffect(effect_index) function, but instead of an effect index, the user needs to pass a level of brightness between 0 and 255. Again, there is a security check to make sure that no number will be set as brightness that is higher than 255 or lower than 0.

### Getters

For every attribute there is a getter. This way the variable values can be requested in a safe way. This is also the only function of the getters: returning the value of a attribute. The getters are used in the set functions as well.

### Other functions

* turnLedOn()
This function turns the LED-strip on. No parameters are needed, there is only a GET request that is sent to the strip to turn it on.

* turnLedOff()
This function turns the LED-strip off. No parameters are needed, there is only a GET request that is sent to the strip to turn it off.
