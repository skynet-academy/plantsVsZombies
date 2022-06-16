import sys
sys.path.append("..")

from .plant import Plant
from arcade import load_texture
import settings

IMAGES = settings.IMAGES

class Torchwood(Plant):
    def __init__(self):
        super().__init__(health=120, cost=175)
        self.texture = load_texture(IMAGES + "tree1.png")

        for i in range(2):
            self.textures.append(load_texture(IMAGES + "tree1.png"))
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "tree2.png"))
        for i in range(2):
            self.texture.append(load_texture(IMAGES + "tree3.png"))
