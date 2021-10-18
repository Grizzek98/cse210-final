from os import path

SPRITE_SCALING = 0.08

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Batter - Group 07"

MOVEMENT_SPEED = 10
ENEMY_SPEED = 10

ANGLE_SPEED = 5


#according to arcade sprites:
#orientation
SPRITE_UP = 0
SPRITE_LEFT = 90
SPRITE_DOWN = 180
SPRITE_RIGHT = 270

#projectile
PLAYER_PROJECTILE_SPEED = 40
PROJECTILE_SCALE = .05
ENEMY_PROJECTILE_SPEED = 25


ROOT_DIRECTORY = path.abspath(path.join(path.dirname(__file__),".."))
RESOURCE_DIRECTORY = path.join(ROOT_DIRECTORY, "resources")
