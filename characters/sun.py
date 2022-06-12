import sys
sys.path.append("..")
from arcade import Sprite
from game import settings

IMAGES = settings.IMAGES

class Sun(Sprite):
    def __init__(self, position_x, position_y):
        super().__init__(IMAGES + "sun.png", 0.12)
        self.center_x = position_x
        self.center_y = position_y

    def update(self):
        self.angle += 1
