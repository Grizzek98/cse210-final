import arcade
from game.floating_object import FloatingObject
from game import constants
import math
from os import path
class Projectile(FloatingObject):
    """a projectile sprite
        attr:
        self, an instance of Projectile
        center_x, starting position of sprite
        center_y, starting position of sprite
        angle, starting orientation of sprite"""
    def __init__(self, center_x, center_y, angle, speed=constants.PLAYER_PROJECTILE_SPEED):
        super().__init__(filename= path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "projectile.png")),
        scale= constants.PROJECTILE_SCALE,
        center_x= center_x,
        center_y= center_y,
        angle= angle,)
        self.speed = speed
        self.set_velocity()
        pass

    def set_velocity(self):
        #angle to radians
        #sin/cos flipped because arcade's 0 is vertical
        self.change_y = math.sin(self.radians + math.pi / 2) * self.speed
        self.change_x = math.cos(self.radians + math.pi / 2) * self.speed


