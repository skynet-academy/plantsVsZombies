# Importing arcade functions and classes
from arcade import (
        Window, 
        load_texture, 
        SpriteList,
        start_render,
        draw_texture_rectangle,
        draw_text,
        color,
        play_sound,
        )

# Importing some useful libraries
from time import time
from random import randint
from .planting import lawn_x, lawn_y
from . import settings
import sys
sys.path.append("..")

# Constants
BACKGROUND = f"{settings.IMAGES}/background.jpg"
MENU = f"{settings.IMAGES}/menu_vertical.png"
BACKGROUND_FINISH = f"{settings.IMAGES}/end.png"
LOGO = f"{settings.IMAGES}/logo.png"

# Characters
from characters.buckhead_zombie import BuckheadZombie
from characters.conehead_zombie import ConeheadZombie
from characters.ordinary_zombie import OrdinaryZombie

from characters.sunflower import SunFlower
from characters.peashoter import PeaShooter
from characters.torchwood import Torchwood
from characters.wallnut import WallNut



class PlantsVsZombies(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = True
        self.back = load_texture(BACKGROUND)
        self.menu = load_texture(MENU)
        self.plants = SpriteList()
        self.seed = None
        self.lawns = []
        self.sun = 300
        self.spawns_suns = SpriteList()
        self.peas = SpriteList()
        self.zombies = SpriteList()
        self.zombie_spawn = time()
        self.end_game = load_texture(BACKGROUND_FINISH)
        self.killed_zombies = 0
        self.attack_time = 20

    def setup(self):
        pass

    def on_draw(self):
        start_render()
        draw_texture_rectangle(
                settings.SCREEN_WIDTH/2,
                settings.SCREEN_HEIGHT/2,
                settings.SCREEN_WIDTH,
                settings.SCREEN_HEIGHT,
                self.back)
        draw_texture_rectangle(60, 300, 130, 600, self.menu)
        draw_text(f"{self.sun}", 30, 490, color.BROWN, 30) 
        self.plants.draw()
        self.spawns_suns.draw()
        self.peas.draw()
        self.zombies.draw()

        if(self.game == False):
            draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 500, 400, self.end_game)

        if(self.seed != None):
            self.seed.draw()

    def update(self, delta_time):
        if(self.game):
            self.plants.update_animation()
            self.plants.update()
            self.peas.update()
            self.peas.update_animation()
            self.zombies.update()
            self.zombies.update_animation()
            for pea in self.peas:
                pea.zombies = self.zombies

            for plant in self.plants:
                if(plant.is_dead):
                    self.lawns.remove((plant.line, plant.column))

            if(time() - self.zombie_spawn > self.attack_time and self.killed_zombies < 20):
                center_y, line = lawn_y(randint(30,520))
                zombie_type = randint(1,3)
                if(zombie_type == 1):
                    zombie = OrdinaryZombie(line)
                elif(zombie_type == 2):
                    zombie = ConeheadZombie(line)
                else:
                    zombie = BuckheadZombie(line)

                zombie.center_y = center_y
                self.zombies.append(zombie)
                self.zombie_spawn = time()
            if(self.killed_zombies >= 20 and len(self.zombies) == 0):
                self.end_game = load_texture(LOGO)
                self.game = False


    def on_mouse_press(self, x, y, button, modifiers):
        if(self.game):
            if(10 < x < 110 and 370 < y < 480):
                self.seed = SunFlower()
                play_sound(self.seed.flower_seed)

            if(10 < x < 110 and 255 < y < 365):
                self.seed = PeaShooter()
                play_sound(self.seed.flower_seed)

            if(10 < x < 110 and 140 < y < 250):
                self.seed = WallNut()
                play_sound(self.seed.flower_seed)

            if(10 < x < 110 and 25 < y < 135):
                self.seed = Torchwood()
                play_sound(self.seed.flower_seed)

            if(self.seed != None):
                self.seed.center_x = x
                self.seed.center_y = y
                self.seed.alpha = 150

    def on_mouse_motion(self, x, y, dx, dy):
        if(self.seed != None):
            self.seed.center_x = x
            self.seed.center_y = y


    def on_mouse_release(self, x, y, button, modifiers):
        if(self.seed is not None and 250 < x < 960 and 30 < y < 526):
            center_x, column = lawn_x(x)
            center_y, line = lawn_y(y)
            cost = self.seed.cost
            if((line, column) not in self.lawns and self.sun >= cost):
                self.sun -= cost
                self.lawns.append((line, column))
                self.seed.planting(center_x, center_y, line, column)
                self.seed.alpha = 255
                self.plants.append(self.seed)
                self.seed = None

            elif(self.seed is not None and 0 < x < 130):
                self.seed = None

        for sun in self.spawns_suns:
            if(sun.left < x < sun.right and sun.bottom < y < sun.top):
                sun.kill()
                self.sun += 25
