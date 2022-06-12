from arcade import Sprite

class Pea(arcade.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__("./bul.png", 0.12)
        self.center_x = position_x
        self.center_y = position_y
        self.damage = 1
        self.change_x = 7
    
    def update(self):
        self.center_x += self.change_x
        if(self.center_x > SCREEN_WIDTH):
            self.kill()

        hits = arcade.check_for_collision_with_list(self, window.zombies)
        if(len(hits) > 0):
            for zombie in hits:
                zombie.health -= self.damage
                self.kill()
