import arcade
import time
import random

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = True
        self.back = arcade.load_texture("./background.jpg")
        self.menu = arcade.load_texture("./menu_vertical.png")
        self.plants = arcade.SpriteList()
        self.seed = None
        self.lawns = []
        self.sun = 300
        self.spawns_suns = arcade.SpriteList()
        self.peas = arcade.SpriteList()
        self.zombies = arcade.SpriteList()
        self.zombie_spawn = time.time()
        self.end_game = arcade.load_texture("./end.png")
        self.killed_zombies = 0
        self.attack_time = 20

    def setup(self):
        pass


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.back)
        arcade.draw_texture_rectangle(60, 300, 130, 600, self.menu)
        arcade.draw_text(f"{self.sun}", 30, 490, arcade.color.BROWN, 30) 
        self.plants.draw()
        self.spawns_suns.draw()
        self.peas.draw()
        self.zombies.draw()

        if(self.game == False):
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 500, 400, self.end_game)


        if(self.seed != None):
            self.seed.draw()

    def update(self, delta_time):
        if(self.game):
            self.plants.update_animation()
            self.plants.update()
            self.peas.update()
            self.peas.update_animation()
            self.zombies.update()
            self.zombies.update_animation()

            if(time.time() - self.zombie_spawn > self.attack_time and self.killed_zombies < 20):
                center_y, line = lawn_y(random.randint(30,520))
                zombie_type = random.randint(1,3)
                if(zombie_type == 1):
                    zombie = OrdinaryZombie(line)
                elif(zombie_type == 2):
                    zombie = ConeheadZombie(line)
                else:
                    zombie = BuckheadZombie(line)

                zombie.center_y = center_y
                self.zombies.append(zombie)
                self.zombie_spawn = time.time()
            if(self.killed_zombies >= 20 and len(self.zombies) == 0):
                self.end_game = arcade.load_texture("./logo.png")
                self.game = False


    def on_mouse_press(self, x, y, button, modifiers):
        if(self.game):
            if(10 < x < 110 and 370 < y < 480):
                print("Sun Flower")
                
                self.seed = SunFlower()
                arcade.play_sound(self.seed.flower_seed) 
            if(10 < x < 110 and 255 < y < 365):
                print("PeaShooter")
                self.seed = PeaShooter()                
            
            if(10 < x < 110 and 140 < y < 250):
                print("WallNut")
                self.seed = WallNut()

            if(10 < x < 110 and 25 < y < 135):
                print("Torchwood") 
                self.seed = Torchwood()

            if(self.seed != None):
                self.seed.center_x = x
                self.seed.center_y = y
                self.seed.alpha = 150
        

    def on_mouse_motion(self, x, y, dx, dy):
        if(self.seed != None):
            self.seed.center_x = x
            self.seed.center_y = y


    def on_mouse_release(self, x, y, button, modifiers):
        if(self.seed is not None and 250 < x < 960 and 30 < y < 526):
            center_x, column = lawn_x(x)
            center_y, line = lawn_y(y)
            cost = self.seed.cost
            if((line, column) not in self.lawns and self.sun >= cost):
                self.sun -= cost
                self.lawns.append((line, column))
                self.seed.planting(center_x, center_y, line, column)
                self.seed.alpha = 255
                self.plants.append(self.seed)
                self.seed = None
            elif(self.seed is not None and 0 < x < 130):
                self.seed = None
        for sun in self.spawns_suns:
            if(sun.left < x < sun.right and sun.bottom < y < sun.top):
                sun.kill()
                self.sun += 25
