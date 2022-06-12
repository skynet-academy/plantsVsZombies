from .plant import Plant


class SunFlower(Plant):
    def __init__(self):
        super().__init__(health=80, cost=50)
        self.texture = arcade.load_texture("./sun1.png")
        for i in range(3):
            self.textures.append(arcade.load_texture("./sun1.png"))

        for i in range(3):
            self.textures.append(arcade.load_texture("./sun2.png"))
        
        self.sun_spawn = time.time()

    def update(self):
        super().update()
        if(time.time() - self.sun_spawn >= 15):
            sun = Sun(self.center_x + 20, self.center_y + 30)
            window.spawns_suns.append(sun)
            self.sun_spawn = time.time()
