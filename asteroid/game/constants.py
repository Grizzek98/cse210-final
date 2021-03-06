from os import path

#directories
ROOT_DIRECTORY = path.abspath(path.join(path.dirname(__file__),".."))
RESOURCE_DIRECTORY = path.join(ROOT_DIRECTORY, "resources")

SPRITE_SCALING = 0.08

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Conquest - Group 07 Final Project"




ENEMY_SPEED = 5

ANGLE_SPEED = 5

#player constants
SHIP_SPRITE_DIRECTORY = path.join(RESOURCE_DIRECTORY, path.join("PNG", "player_ship.png"))

MOVEMENT_SPEED = 6
PLAYER_PROJECTILE_SPEED = 20

PLAYER_ROTATION_SPEED = 5 #in degrees
PLAYER_ACCELERATION = .30

#orientation according to arcade sprites in degrees:
SPRITE_UP = 0
SPRITE_LEFT = 90
SPRITE_DOWN = 180
SPRITE_RIGHT = 270

#projectile
PROJECTILE_SCALE = .05
PLAYER_FIRERATE = 1
ENEMY_PROJECTILE_SPEED = 25

#asteroid
ASTEROID_SPRITE_DIRECTORY = path.join(RESOURCE_DIRECTORY, path.join("PNG", "asteroid.png"))
ASTEROID_MAX_SPAWN_RATE = 0.3
ASTEROID_MAX_VELOCITY = 5

#backgrounds
MAIN_MENU_BG = path.join(RESOURCE_DIRECTORY, path.join("PNG", "main_menu.png"))
SPACE_BG = path.join(RESOURCE_DIRECTORY, path.join("PNG", "space_bg.png"))
INSTRUCIONS_BG = path.join(RESOURCE_DIRECTORY, path.join("PNG", "space_conquest_instructions.png"))

#Sound Effects
BG_MUSIC = path.join(RESOURCE_DIRECTORY, path.join("ST", "bg_music.mp3"))
SHOT_SOUND = path.join(RESOURCE_DIRECTORY, path.join("ST", "laser_shot_effect.mp3"))

#HIGHSCORE_FILE

HIGHSCORE_FILE = path.join(RESOURCE_DIRECTORY,path.join("user_data", "highscore.txt"))

#Power-ups
DOUBLEX_POWER_SPRITE = path.join(RESOURCE_DIRECTORY,path.join("PNG", "2x_buff.png"))
POWERUP_DURATION = 15

HIGHSCORE_FILE = path.join(ROOT_DIRECTORY,path.join("user_data", "highscore.txt"))

