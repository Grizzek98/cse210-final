import arcade
from game.floating_object import FloatingObject
import game.constants
import math
from os import path

class Projectile(FloatingObject):
    """ The base file for the actual sprite created when a weapon is fired.
    
        Stereotypes:
            Information Holder
            
        Attributes:
            TODO
    """

    def __init__(self, filename: str = path.join(game.constants.RESOURCE_DIRECTORY, path.join("PNG", "projectile.png")), scale: float = game.constants.PROJECTILE_SCALE, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture = None, angle: float = 0,
    speed =game.constants.PLAYER_PROJECTILE_SPEED, damage = 10, num_pierce = 0): #non sprite params
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle)
        """ The class constructor.
        
            Args:
                self (Projectile): An instance of PewpewVisual.
        """
        self.speed = speed
        self._damage = damage
        self._num_pierce = num_pierce
        self._set_velocity()

    def _set_velocity(self):
        """set velocity according to orientation"""
        #angle to radians
        #sin/cos flipped because arcade's 0 is vertical
        self.change_y = math.sin(self.radians + math.pi / 2) * self.speed
        self.change_x = math.cos(self.radians + math.pi / 2) * self.speed