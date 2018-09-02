from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Hx711(ArduinoObject):

    def __init__(self, pin_dout, pin_slk, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new',  pin_dout, pin_slk)

    @arduinoobjectmethod
    def setOffset(self, offset):
        pass

    @arduinoobjectmethod
    def setScale(self, scale):
        pass

    @returns(float)
    @arduinoobjectmethod
    def getGram(self):
        pass

    @returns(int)
    @arduinoobjectmethod
    def averageValue(self):
        pass