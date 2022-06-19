# Importing arcade functions and classes
from arcade import (
        Window,
        run,
        load_texture,
        SpriteList,
        start_render,
        draw_texture_rectangle,
        draw_text,
        color,
        play_sound,
        check_for_collision_with_list,
        load_sound
        )

# Importing some useful libraries
from time import time
from random import randint
from utilities.plant_position import lawn_x, lawn_y
from utilities.collisions import collision_with_zombies

# Importing Settings
import settings

# Characters
from characters.buckhead_zombie import BuckheadZombie
from characters.conehead_zombie import ConeheadZombie
from characters.ordinary_zombie import OrdinaryZombie

from characters.pea import Pea
from characters.sun import Sun
from characters.sunflower import SunFlower
from characters.peashoter import PeaShooter
from characters.torchwood import Torchwood
from characters.wallnut import WallNut


class PlantsVsZombies(Window):
    def __init__(self, st):
        super().__init__(st.SCREEN_WIDTH, st.SCREEN_HEIGHT, st.SCREEN_TITLE)
        self.game = True
        self.back = load_texture(st.BACKGROUND)
        self.menu = load_texture(st.MENU_IMAGE)
        self.plants = SpriteList()
        self.seed = None
        self.lawns = []
        self.sun = st.INITIAL_POINTS
        self.spawns_suns = SpriteList()
        self.peas = SpriteList()
        self.zombies = SpriteList()
        self.zombie_spawn = time()
        self.end_game = load_texture(st.BACKGROUND_GAME_OVER)
        self.killed_zombies = 0
        self.attack_time = st.ATTACK_TIME
        self.width = st.SCREEN_WIDTH
        self.height = st.SCREEN_HEIGHT
        self.st = st
        self.music_game = load_sound(self.st.SOUNDS + 'grasswalk.mp3')

    def setup(self):
        play_sound(self.music_game)

    def on_draw(self):
        start_render()
        draw_texture_rectangle(
                self.width/2,
                self.height/2,
                self.width,
                self.height,
                self.back)
        draw_texture_rectangle(60, 300, 130, 600, self.menu)
        draw_text(f"{self.sun}", 30, 490, color.BROWN, 30) 
        self.plants.draw()
        self.spawns_suns.draw()
        self.peas.draw()
        self.zombies.draw()

        if(self.game == False):
            draw_texture_rectangle(
                    self.width/2,
                    self.height/2,
                    500,
                    400,
                    self.end_game
                    )

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

            for plant in self.plants:
                if(plant.add_sun):
                    sun = Sun(plant.center_x + 20, plant.center_y + 30)
                    self.spawns_suns.append(sun)
                    plant.add_sun = False

                if(plant.add_pea):
                    pea = Pea(plant.center_x + 10, plant.center_y + 10)
                    self.peas.append(pea)
                    plant.add_pea = False

                if(plant.is_dead):
                    self.lawns.remove((plant.line, plant.column))
                
                fire_peas = check_for_collision_with_list(plant, self.peas)
                for pea in fire_peas:
                    if(plant.add_fire):
                        pea.texture = load_texture(settings.IMAGES + "firebul.png")
                        pea.demage = 3

                zombies = check_for_collision_with_list(plant, self.zombies)
                for zombie in zombies:
                    zombie.eating = True
                    if(zombie.game_over):
                        [plant.kill() for plant in self.plants]

            for zombie in self.zombies:
                if(zombie.game_over):
                    self.back = self.end_game
                plants = check_for_collision_with_list(zombie, self.plants)
                for plant in plants:
                    if(plant.line == zombie.line):
                        plant.health -= self.st.ZOMBIE_ATTACK
                        plant.same_line = True
                    if(plant.is_dead):
                        plant.kill()
                        zombie.eating = False

            for pea in self.peas:
                zombies = check_for_collision_with_list(pea, self.zombies)
                for zombie in zombies:
                    zombie.health -= pea.damage
                    play_sound(pea.sound)
                    pea.hit = True

            if(time() - self.zombie_spawn > self.attack_time and self.killed_zombies < 20):
                center_y, line = lawn_y(randint(30,520))
                zombie_type = randint(1,3)
                if(zombie_type == 1):
                    zombie = OrdinaryZombie(line, self.width)
                elif(zombie_type == 2):
                    zombie = ConeheadZombie(line, self.width)
                else:
                    zombie = BuckheadZombie(line, self.width)

                zombie.center_y = center_y
                self.zombies.append(zombie)
                self.zombie_spawn = time()

    def on_mouse_press(self, x, y, button, modifiers):
        if(self.game):
            if(self.st.M_LIMIT_L < x < self.st.M_LIMIT_R and 370 < y < 480):
                self.seed = SunFlower()
                play_sound(self.seed.flower_seed)

            if(self.st.M_LIMIT_L < x < self.st.M_LIMIT_R and 255 < y < 365):
                self.seed = PeaShooter()
                play_sound(self.seed.flower_seed)

            if(self.st.M_LIMIT_L < x < self.st.M_LIMIT_R and 140 < y < 250):
                self.seed = WallNut()
                play_sound(self.seed.flower_seed)

            if(self.st.M_LIMIT_L < x < self.st.M_LIMIT_R and 25 < y < 135):
                self.seed = Torchwood()
                self.seed.add_fire = True
                play_sound(self.seed.flower_seed)

            if(self.seed != None):
                self.seed.center_x = x
                self.seed.center_y = y
                self.seed.alpha = self.st.ALPHA

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
                self.seed.alpha = self.st.ALPHA_PLANTING
                self.plants.append(self.seed)
                self.seed = None

            elif(self.seed is not None and 0 < x < 130):
                self.seed = None

        for sun in self.spawns_suns:
            if(sun.left < x < sun.right and sun.bottom < y < sun.top):
                sun.kill()
                self.sun += self.st.SUN_POINT

if __name__ == '__main__':
    window = PlantsVsZombies(settings)
    window.setup()
    run()
