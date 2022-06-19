import sys
sys.path.append("..")

import settings
from .plant import Plant
from arcade import load_texture, AnimationKeyframe

IMAGES = settings.IMAGES

class WallNut(Plant):
    def __init__(self):
        super().__init__(health=200, cost= 50)
        self.frames = [
                AnimationKeyframe(1, 200, load_texture(IMAGES + "nut1.png")),
                AnimationKeyframe(2, 200, load_texture(IMAGES + "nut2.png")),
                AnimationKeyframe(3, 200, load_texture(IMAGES + "nut3.png")),
                AnimationKeyframe(4, 200, load_texture(IMAGES + "nut1.png")),
                ]
