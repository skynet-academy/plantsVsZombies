import sys
sys.path.append("..")

import settings
from .plant import Plant
from arcade import load_texture, AnimationKeyframe
from time import time

IMAGES = settings.IMAGES


class PeaShooter(Plant):
    def __init__(self):
        super().__init__(health=100, cost=100)
        self.frames = [
            AnimationKeyframe(1, 200, load_texture(IMAGES + "pea1.png")),
            AnimationKeyframe(2, 200, load_texture(IMAGES + "pea2.png")),
            AnimationKeyframe(3, 200, load_texture(IMAGES + "pea3.png")),
        ]

        self.pea_spawn = time()

    def update(self):
        super().update()
        if(time() - self.pea_spawn >= 2):
            self.add_pea = True
            self.pea_spawn = time()

