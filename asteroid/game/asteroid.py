
from game.floating_object import FloatingObject

class Asteroid(FloatingObject):
    """ A hunk of space rock (in addition to other elements) that try to make the player's ship have a bad day.
    
        Stereotypes:
            Information Holder
        
        Attributes:
            NONE
    """

    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)
        """ The class constructor.
        
            Args: 
                self (Asteroid): An instance of Asteroid.
        """

    def on_update(self, delta_time):
        """ Handles what happens on update
        
            Args:
                self (Asteroid): An instance of Asteroid.
        """
        self.rotate()
        self.move_x()
        self.move_y()