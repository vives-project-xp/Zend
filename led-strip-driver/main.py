import requests
import time

from src.led import LedStrip

url = "http://172.16.101.72"
zend_ledstrip = LedStrip(8, url)
time.sleep(2)
zend_ledstrip.setBrightness(50)
time.sleep(2)
zend_ledstrip.setPrimaryColor("FFFFFF")
time.sleep(2)
zend_ledstrip.setSecondaryColor("C2B280")
time.sleep(2)
zend_ledstrip.setEffect(2)
time.sleep(1)
