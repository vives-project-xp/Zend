import string
import requests

class LedStrip:

    def __init__(self, number_of_leds, led_url: string):

        # Attributes
        self.__led_count = number_of_leds
        self.__url = led_url
        self.__brightness = 50  # default start at 50
        self.__effect_index = 0

        # First get request to set LEDs to white (= default)
        full_url = self.__url + '/win&S=0&S2={}&A={}&CL=hFFFFFF&T=1'.format(str(self.getLedCount()), str(self.getBrightness()))
        r = requests.get(url = full_url)
        print("URL = " + full_url)

    def setLedCount(self, number_of_leds):
        self.__led_count = number_of_leds
        full_url = str(self.getUrl()) + '/win&S=0&S2={}&T=1'.format(str(self.getLedCount))
        r = requests.get(url = full_url)

    def setPrimaryColor(self, hex_color: string):
        full_url = str(self.getUrl()) + '/win&CL=h{}&A={}&T=1'.format(hex_color, str(self.getBrightness))
        r = requests.get(url = full_url)

    def setSecondaryColor(self, hex_color: string):
        full_url = str(self.getUrl()) + '/win&C2=h{}&A={}&T=1'.format(hex_color, str(self.getBrightness))
        r = requests.get(url = full_url)

    def setThirdColor(self, hex_color: string):
        full_url = str(self.getUrl()) + '/win&C3=h{}&A={}&T=1'.format(hex_color, str(self.getBrightness))
        r = requests.get(url = full_url)

    def setEffect(self, effect_index):
        if effect_index >= 73:
            self.__effect_index = 73
        elif effect_index <= 0:
            self.__effect_index = 0
        else:
            self.__effect_index = effect_index
        full_url = str(self.getUrl()) + '/win&FX={}&T=1'.format(str(self.__effect_index))
        r = requests.get(url = full_url)
        print("Effect URL = " + full_url)
        print("Brightness at effect is: " + str(self.getBrightness()))

    def setBrightness(self, brightness):
        if brightness >= 255:
            self.__brightness = 255
        elif brightness <= 0:
            self.__brightness = 0
        else:
            self.__brightness = brightness

        full_url = str(self.getUrl()) + '/win&A={}&T=1'.format(str(self.getBrightness()))
        r = requests.get(url = full_url)
        print("Brightness is: " + str(self.getBrightness()))

    def turnLedOff(self):
        full_url = str(self.getUrl()) + '/win&T=0'
        r = requests.get(url = full_url)

    def turnLedOn(self):
        full_url = str(self.getUrl()) + '/win&T=1'
        r = requests.get(url = full_url)

    def getLedCount(self):
        return self.__led_count

    def getUrl(self):
        return self.__url

    def getBrightness(self):
        return self.__brightness

    def getEffectIndex(self):
        return self.__effect_index

