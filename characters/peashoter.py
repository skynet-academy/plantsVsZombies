import sys
sys.path.append("..")

import settings
from .plant import Plant
from arcade import load_texture
from time import time

IMAGES = settings.IMAGES


class PeaShooter(Plant):
    def __init__(self):
        super().__init__(health=100, cost=100)
        self.texture = load_texture(IMAGES + "pea1.png")
        self.texture = load_animated_gif(IMAGES + "peashooter.gif")
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "pea1.png"))
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "pea2.png"))
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "pea3.png"))

        self.pea_spawn = time()

    def update(self):
        super().update()
        if(time() - self.pea_spawn >= 2):
            self.add_pea = True
            self.pea_spawn = time()

