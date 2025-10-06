# A Script Used For Defining The Sin Wave Data Structure. #\
import math

ScreenScale = 1

class SinWave():
    movespeed : float
    offset    : float
    scale     : float
    mult      : float

    def __init__(self, offset, scale, multitude):
        self.movespeed = 0 # Needs To Be Set Later.
        self.offset    = offset
        self.scale     = scale
        self.mult      = multitude

    def ToSin(self, x) -> float:
        return math.sin((x * (self.scale*ScreenScale)) + self.offset + self.movespeed) * self.mult
    
    def print(self):
        print(f"Sin Function: [Scale: {self.scale}, Offset: {self.offset}, Multitude: {self.mult}]")

SinWaves = [

    SinWave(+0, 0.10, 5.00),
    SinWave(-2, 0.50, 1.00),
    SinWave(+5, 0.05, 1.75)

]