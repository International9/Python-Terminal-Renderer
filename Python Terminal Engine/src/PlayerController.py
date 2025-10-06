from src.VectorLib import *
from src.Constants import *
import src.Input as Input

class Player:
    speed = 5
    position = Vector2.zero()

    def __init__(self, pos, spd):
        self.position = pos
        self.speed = spd

    @property
    def wishDir(self) -> Vector2:
        fin = Vector2.zero()

        if (Input.IsKeyDown('w')):
            fin.y = 1

        if (Input.IsKeyDown('s')):
            fin.y = -1

        if (Input.IsKeyDown('a')):
            fin.x = -1

        if (Input.IsKeyDown('d')):
            fin.x = 1

        return fin

    def move(self):
        self.position += self.wishDir * DELTA_TIME * self.speed
