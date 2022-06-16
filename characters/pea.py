import sys
sys.path.append("..")

import settings
from arcade import Sprite, load_sound

IMAGES = settings.IMAGES
SOUND = settings.SOUNDS

class Pea(Sprite):
    def __init__(self, position_x, position_y):
        super().__init__(IMAGES + "bul.png", 0.12)
        self.center_x = position_x
        self.center_y = position_y
        self.damage = 1
        self.sound = load_sound(SOUND + "hit.mp3")
        self.change_x = 7
        self.hit = False
    
    def update(self):
        self.center_x += self.change_x
        if(self.center_x > settings.SCREEN_WIDTH):
            self.kill()
        if(self.hit):
            self.kill()
