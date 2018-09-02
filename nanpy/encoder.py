from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Encoder(ArduinoObject):

    def __init__(self, pin1, pin2, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', pin1, pin2)

    @returns(int)
    @arduinoobjectmethod
    def read(self):
        pass