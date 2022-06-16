import sys
sys.path.append("..")

import settings
from .zombie import Zombie
from arcade import load_texture

IMAGES = settings.IMAGES

class BuckheadZombie(Zombie):
    
    def __init__(self, line, position):
        super().__init__(health=32, line=line, center_x=position)
        self.texture = load_texture(IMAGES + "buck1.png")

        for i in range(5):
            self.textures.append(load_texture(IMAGES + "buck1.png"))
        self.textures.append(load_texture(IMAGES + "buck2.png"))
