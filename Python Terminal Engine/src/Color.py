import math

class Color:
    r : float
    g : float
    b : float

    def __init__(self, _r, _g, _b):
        self.r = _r
        self.g = _g
        self.b = _b

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

    @staticmethod
    def hsvToRgb(h, s, v):
        i = math.floor(h * 6)
        f = h * 6 - i
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)

        sector = i % 6

        if sector == 0:
            r, g, b = v, t, p
        elif sector == 1:
            r, g, b = q, v, p
        elif sector == 2:
            r, g, b = p, v, t
        elif sector == 3:
            r, g, b = p, q, v
        elif sector == 4:
            r, g, b = t, p, v
        elif sector == 5:
            r, g, b = v, p, q

        return Color(int(r * 255), int(g * 255), int(b * 255))

    @staticmethod
    def red(): return Color(255, 0, 0)

    @staticmethod
    def green(): return Color(0, 255, 0)

    @staticmethod
    def blue(): return Color(0, 0, 255)

    @staticmethod
    def black(): return Color(0, 0, 0)

    @staticmethod
    def white(): return Color(255, 255, 255) 
