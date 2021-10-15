import arcade
from game import constants

class FloatingObject(arcade.Sprite):
    """ An object on the screen. May or may not move.
    
        Stereotypes:
            Information Holder
        
        Attributes:
            NONE
    """

    def update(self):
        """ Handles what the object does every update.
        
            Args: 
                self (MovingSprite): An instance of MovingSprite.
        """
        self.move_x()
        self.move_y()
        self.check_bounds_x()
        self.check_bounds_y()

    def move_x(self):
        """ Moves the object along the x axis.
        
            Args: 
                self (MovingSprite): An instance of MovingSprite.
        """
        self.center_x += self.change_x

    def move_y(self):
        """ Moves the object along the y axis.
        
            Args:
                self (MovingSprite): An instance of MovingSprite.
        """
        self.center_y += self.change_y

    def check_bounds_x(self):
        """ Checks if object is beyond x bounds.
        
            Args:
                self (MovingSprite): An instance of MovingSprite.
        """
        if self.left < 0 or self.right > constants.SCREEN_WIDTH - 1:
            return True
    
    def check_bounds_y(self):
        """ Checks if object is beyond y bounds.
        
            Args:
                self (MovingSprite): An instance of MovingSprite.
        """
        if self.top > constants.SCREEN_HEIGHT - 1:
            return True
        if self.bottom < 0:
            return False
