import sys
sys.path.append("..")

import settings
from .plant import Plant
from .sun import Sun
from arcade import load_texture, AnimationKeyframe
from time import time

IMAGES = settings.IMAGES

class SunFlower(Plant):
    def __init__(self):
        super().__init__(health=80, cost=50)
        self.frames = [
                AnimationKeyframe(1, 200, load_texture(IMAGES + "sun2.png")),
                AnimationKeyframe(2, 200, load_texture(IMAGES + "sun1.png")),
                AnimationKeyframe(3, 200, load_texture(IMAGES + "sun2.png")),
                ]
        
        self.sun_spawn = time()

    def update(self):
        super().update()
        if(time() - self.sun_spawn >= 15):
            self.add_sun = True
            self.sun_spawn = time()
