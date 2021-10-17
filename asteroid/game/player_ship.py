
from game import constants
from game.floating_object import FloatingObject

class PlayerShip(FloatingObject):
    """ A player-controlled ship that moves around the screen.
    
        Stereotypes:
            Information Holder
        
        Attributes:
            NONE
    """
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)
        self.is_shooting = False


    def update(self):
        """ Handles what happens on update
        
            Args:
                self (PlayerShip): An instance of PlayerShip.
        """
        self.angle += self.change_angle
        self.move_x()
        self.move_y()
        self.check_bounds_x()
        self.check_bounds_y()

    def check_bounds_x(self):
        if self.left < 0:
            self.left = 0
        if self.right > constants.SCREEN_WIDTH - 1:
            self.right = constants.SCREEN_WIDTH

    def check_bounds_y(self):
        if self.bottom < 0:
            self.bottom = 0
        if self.top > constants.SCREEN_HEIGHT - 1:
            self.top = constants.SCREEN_HEIGHT