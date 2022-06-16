import sys
sys.path.append("..")

import settings
from arcade import AnimatedTimeSprite, load_texture, load_sound, play_sound
SOUND = settings.SOUNDS


class Plant(AnimatedTimeSprite):
    def __init__(self, health, cost):
        super().__init__(0.12)
        self.health = health
        self.cost = cost
        self.line = 0
        self.column = 0
        self.flower_seed = load_sound(SOUND + "seed.mp3")
        self.is_dead = False
        self.same_line = False
        self.add_pea = False
        self.add_sun = False
        self.add_fire = False

    def update(self):
        if(self.health <= 0):
            self.is_dead = True


    def planting(self, center_x, center_y, line, column):
        play_sound(self.flower_seed) 
        self.center_x = center_x
        self.center_y = center_y
        self.line = line
        self.column = column
