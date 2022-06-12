from .zombie import Zombie


class BuckheadZombie(Zombie):
    
    def __init__(self, line):
        super().__init__(health=32, line=line)
        self.texture = arcade.load_texture("./buck1.png")

        for i in range(5):
            self.textures.append(arcade.load_texture("./buck1.png"))
        self.textures.append(arcade.load_texture("./buck2.png"))
