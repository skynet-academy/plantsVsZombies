from arcade import AnimatedTimeSprite


class Plant(AnimatedTimeSprite):
    def __init__(self, health, cost):
        super().__init__(0.12)
        self.health = health
        self.cost = cost
        self.line = 0
        self.column = 0
        self.flower_seed = arcade.load_sound("./seed.mp3")

    def update(self):
        if(self.health <= 0):
            self.kill()
            window.lawns.remove((self.line, self.column))


    def planting(self, center_x, center_y, line, column):
        arcade.play_sound(self.flower_seed) 
        self.center_x = center_x
        self.center_y = center_y
        self.line = line
        self.column = column
