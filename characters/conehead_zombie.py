import sys
sys.path.append("..")

import settings
from .zombie import Zombie
from arcade import load_texture

IMAGES = settings.IMAGES


class ConeheadZombie(Zombie):
    def __init__(self, line, position):
        super().__init__(health=20, line=line, center_x=position)
        self.texture = load_texture(IMAGES + "cone1.png")
        for i in range(5):
            self.textures.append(load_texture(IMAGES + "cone1.png"))
        self.textures.append(load_texture(IMAGES + "cone2.png"))
