from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class RGBLED(ArduinoObject):

    def __init__(self, redpin, greenpin, bluepin, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', redpin, greenpin, bluepin)

    @arduinoobjectmethod
    def addLED(self, redpin, greenpin, bluepin):
        pass

    @arduinoobjectmethod
    def update(self):
        pass

    @arduinoobjectmethod
    def setColor(self, red, green, blue):
        pass

    @arduinoobjectmethod
    def fadeToColor(self, red, green, blue, time):
        pass

    @arduinoobjectmethod
    def pulse(self, red, green, blue, time):
        pass

    @arduinoobjectmethod
    def blink(self, red, green, blue, time):
        pass

    @arduinoobjectmethod
    def rainbow(self, time):
        pass

    @arduinoobjectmethod
    def off(self):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getCurrentRed(self):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getCurrentGreen(self):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getCurrentBlue(self):
        pass