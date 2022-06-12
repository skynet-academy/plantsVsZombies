class ConeheadZombie(Zombie):
    def __init__(self, line):
        super().__init__(health=20, line=line)
        self.texture = arcade.load_texture("./cone1.png")
        for i in range(5):
            self.textures.append(arcade.load_texture("./cone1.png"))
        self.textures.append(arcade.load_texture("./cone2.png"))
