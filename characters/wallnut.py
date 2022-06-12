import sys
sys.path.append("..")

from .plant import Plant
from game import settings
from arcade import load_texture

IMAGES = settings.IMAGES

class WallNut(Plant):
    def __init__(self):
        super().__init__(health=200, cost= 50)
        self.texture = load_texture(IMAGES + "nut1.png")

        for i in range(10):
            self.textures.append(load_texture(IMAGES + "nut1.png"))
        self.textures.append(load_texture(IMAGES + "nut2.png"))
        
        for i in range(10):
            self.textures.append(load_texture(IMAGES + "nut3.png"))
        self.textures.append(load_texture(IMAGES + "nut2.png"))
