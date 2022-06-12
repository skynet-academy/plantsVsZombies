import sys
sys.path.append("..")

from game import settings
from .zombie import Zombie
from arcade import load_texture

IMAGES = settings.IMAGES
class ConeheadZombie(Zombie):
    def __init__(self, line):
        super().__init__(health=20, line=line)
        self.texture = load_texture(IMAGES + "cone1.png")
        for i in range(5):
            self.textures.append(load_texture(IMAGES + "cone1.png"))
        self.textures.append(load_texture(IMAGES + "cone2.png"))
