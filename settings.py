from os.path import join, dirname, abspath

BASE_DIR = dirname(dirname(abspath(__file__)))
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plants VS Zombies"
IMAGES = f'{BASE_DIR}/plantsVsZombies/assets/images/'
SOUNDS = f'{BASE_DIR}/plantsVsZombies/assets/sounds/'
BACKGROUND = IMAGES + 'background.jpg'
MENU_IMAGE = IMAGES + 'menu_vertical.png'
INITIAL_POINTS = 300
BACKGROUND_GAME_OVER = IMAGES + 'end.png'
ATTACK_TIME = 20
ALPHA = 150
ALPHA_PLANTING = 255
M_LIMIT_L = 10
M_LIMIT_R = 110
SUN_POINT = 25
ZOMBIE_ATTACK = 0.5
