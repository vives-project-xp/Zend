# Webinterface

## Client

A simple HTML/JS webpage has been made on which the user can control the functionalities of the Sand Table.

### Led controls

All LED functionality is controlled via the webinterface. The user can turn the LED on or off, choose the brightness, primary and secondary colors, effect and effect speed. The javascript script behind the webpage sends a GET request to the WLED API to change all these parameters.

The led-strip is connected to an [ESP8266](https://en.wikipedia.org/wiki/ESP8266) so that it can be connected to the internet. Then we can send all kinds of GET requests to the WLED API to change the behavior of the LED-strip. Different types of parameters that are added in the URL for the GET request can change the behavior of the LED-strip. An overview of all changeable elements of the LED-strip can be found [here](https://kno.wled.ge/interfaces/http-api/). An overview of all effects to be be set can be found [here](https://github.com/Aircoookie/WLED/wiki/List-of-effects-and-palettes).

### Sand patterns controls

(tbd)

## Server

To initialize FastAPI:

[Source](https://github.com/tiangolo/fastapi)

```pt

pip install fastapi
pip install "uvicorn[standard]"

```

Start server:

```pt
uvicorn server.main:app --reload
```

Start node on client side

```code
http-server
```


