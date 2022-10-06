# import js2py

# result, led_driver = js2py.run_file("main.js")
# result = led_driver.changeColor("FF0000")
# print(result)

import requests

URL = "http://172.16.100.246/win&CL=hC2B280&C2=hFFE3FF&SX=20&FX=2&A=50"
r = requests.get(url = URL)
