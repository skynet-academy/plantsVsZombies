import sys
sys.path.append("..")

from .plant import Plant
from arcade import load_texture
from game import settings

IMAGES = settings.IMAGES 

class Torchwood(Plant):
    def __init__(self):
        super().__init__(health=120, cost=175)
        self.texture = load_texture(IMAGES + "tree1.png")

        for i in range(2):
            self.textures.append(load_texture(IMAGES + "tree1.png"))
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "tree2.png"))
        for i in range(2):
            self.textures.append(load_texture(IMAGES + "tree3.png"))

    def update(self):
        super().update()
        fire_peas = arcade.check_for_collision_with_list(self, PlantsVsZombies.peas)
        for pea in fire_peas:
            pea.texture = load_texture(IMAGES + "firebul.png")
            pea.damage = 3

