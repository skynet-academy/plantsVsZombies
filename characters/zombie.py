from arcade import AnimatedTimeBasedSprite

class Zombie(AnimatedTimeBasedSprite):
    def __init__(self,health, line, center_x):
        super().__init__(scale=0.09)
        self.health = health
        self.line = line
        self.center_x = center_x
        self.change_x = 0.2
        self.eating = False
        self.is_dead = False
        self.game_over = False
        self.stop = False

    def update(self):
        self.center_x -= self.change_x
        if(self.health <= 0):
            self.is_dead = True
            self.kill()

        if(self.stop):
            self.change_x = 0

        if(self.eating):
            self.change_x = 0
            self.angle = 15
        else:
            self.change_x = 0.2
            self.angle = 0

        if(self.center_x < 200):
            self.game_over = True
            self.stop = True

