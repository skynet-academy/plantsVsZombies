import arcade 
from game.game import PlantsVsZombies
from game import settings
if __name__ == '__main__':
    
    window = PlantsVsZombies(
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT,
            settings.SCREEN_TITLE
            )
    window.setup()
    arcade.run()



