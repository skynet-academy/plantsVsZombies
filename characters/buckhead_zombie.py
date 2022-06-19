import sys
sys.path.append("..")

import settings
from .zombie import Zombie
from arcade import load_texture, AnimationKeyframe

IMAGES = settings.IMAGES

class BuckheadZombie(Zombie):
    
    def __init__(self, line, position):
        super().__init__(health=32, line=line, center_x=position)
        self.frames = [
                AnimationKeyframe(1, 200, load_texture(IMAGES + "buck1.png")),
                AnimationKeyframe(2, 200, load_texture(IMAGES + "buck2.png")),
                ]
