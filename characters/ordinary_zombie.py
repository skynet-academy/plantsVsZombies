class OrdinaryZombie(Zombie):
   
    def __init__(self, line):
        super().__init__(health=12, line=line)
        self.texture = arcade.load_texture("./zom1.png")
        for i in range(5):
            self.textures.append(arcade.load_texture("./zom1.png"))
        self.textures.append(arcade.load_texture("./zom2.png"))

