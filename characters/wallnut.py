from .plant import Plant


class WallNut(Plant):
    def __init__(self):
        super().__init__(health=200, cost= 50)
        self.texture = arcade.load_texture("./nut1.png")

        for i in range(10):
            self.textures.append(arcade.load_texture("./nut1.png"))
        self.textures.append(arcade.load_texture("./nut2.png"))
        
        for i in range(10):
            self.textures.append(arcade.load_texture("./nut3.png"))
        self.textures.append(arcade.load_texture("./nut2.png"))
