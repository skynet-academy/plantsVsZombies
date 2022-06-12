from arcade import Sprite


class Sun(arcade.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__("./sun.png", 0.12)
        self.center_x = position_x
        self.center_y = position_y

    def update(self):
        self.angle += 1
