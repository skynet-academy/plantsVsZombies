import sys
sys.path.append("..")

from .plant import Plant
from arcade import load_texture, AnimationKeyframe
import settings

IMAGES = settings.IMAGES

class Torchwood(Plant):
    def __init__(self):
        super().__init__(health=120, cost=175)
        self.frames = [
                AnimationKeyframe(1, 200, load_texture(IMAGES + "tree1.png")),
                AnimationKeyframe(2, 200, load_texture(IMAGES + "tree2.png")),
                AnimationKeyframe(3, 200, load_texture(IMAGES + "tree3.png"))
                ]
