class Torchwood(Plant):
    def __init__(self):
        super().__init__(health=120, cost=175)
        self.texture = arcade.load_texture("./tree1.png")

        for i in range(2):
            self.textures.append(arcade.load_texture("./tree1.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("./tree2.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("./tree3.png"))

    def update(self):
        super().update()
        fire_peas = arcade.check_for_collision_with_list(self, window.peas)
        for pea in fire_peas:
            pea.texture = arcade.load_texture("./firebul.png")
            pea.damage = 3

