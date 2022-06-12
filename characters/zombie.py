
class Zombie(arcade.AnimatedTimeSprite):
   
    def __init__(self,health, line):
        super().__init__(0.09)
        self.health = health
        self.line = line
        self.center_x = SCREEN_WIDTH
        self.change_x = 0.2
   

    def update(self):
        self.center_x -= self.change_x
        if(self.health <=0):
            self.kill()
            window.killed_zombies += 1
            window.attack_time -= 1
        eating = False
        food = arcade.check_for_collision_with_list(self, window.plants)
        for plant in food:
            if(self.line == plant.line):
                plant.health -= 0.5
                eating = True
        if(eating):
            self.change_x = 0
            self.angle = 15
        else:
            self.change_x = 0.2
            self.angle = 0
        if(self.center_x < 200):
            window.game = False
