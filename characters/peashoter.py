import sys
sys.path.append("..")

from game import settings
from .plant import Plant
from arcade import load_texture
from time import time
from .pea import Pea

IMAGES = settings.IMAGES


class PeaShooter(Plant):

    def __init__(self):
        super().__init__(health=100, cost=100)
        self.texture = load_texture(IMAGES + "pea1.png")
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "pea1.png"))
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "pea2.png"))
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "pea3.png"))

        self.pea_spawn = time()

    def update(self):
        super().update()
        zombie_on_line = False
        for zombie in window.zombies:
            if(zombie.line == self.line):
                zombie_on_line = True
        if(time() - self.pea_spawn >= 2 and zombie_on_line):
            pea = Pea(self.center_x + 10, self.center_y + 10)
            window.peas.append(pea)
            self.pea_spawn = time.time()

