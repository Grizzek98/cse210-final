import arcade
from asteroid.game import floating_object
from asteroid.game.constants import PLAYER_PROJECTILE_SPEED
import constants
import math
from os import path
class Projectile(floating_object):
    """a projectile sprite
        attr:
        self, an instance of Projectile
        center_x, starting position of sprite
        center_y, starting position of sprite
        angle, starting orientation of sprite"""
    def __init__(self, center_x, center_y, angle, speed=PLAYER_PROJECTILE_SPEED):
        super().__init__(filename= path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "projectile.png")),
        scale= constants.PROJECTILE_SCALE,
        center_x= center_x,
        center_y= center_y,
        angle= angle,)
        self.speed = speed
        pass

    def set_velocity(self):
        #angle to radians
        #sin/cos flipped because arcade's 0 is vertical
        self.change_y = math.cos(self.radians) * self.speed
        self.change_x = math.sin(self.radians) * self.speed


