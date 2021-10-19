from os import path
#directories
ROOT_DIRECTORY = path.abspath(path.join(path.dirname(__file__),".."))
RESOURCE_DIRECTORY = path.join(ROOT_DIRECTORY, "resources")

SPRITE_SCALING = 0.08

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Batter - Group 07"


ENEMY_SPEED = 10

ANGLE_SPEED = 5

#player constants
SHIP_SPRITE_DIRECTORY = path.join(RESOURCE_DIRECTORY, path.join("PNG", "player_ship.png"))
MOVEMENT_SPEED = 20
PLAYER_PROJECTILE_SPEED = 40
PLAYER_ROTATION_SPEED = 5 #in degrees


#orientation according to arcade sprites in degrees:
SPRITE_UP = 0
SPRITE_LEFT = 90
SPRITE_DOWN = 180
SPRITE_RIGHT = 270

#projectile
PROJECTILE_SCALE = .05
ENEMY_PROJECTILE_SPEED = 25
