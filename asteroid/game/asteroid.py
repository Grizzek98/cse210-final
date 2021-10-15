
from game.floating_object import FloatingObject

class Asteroid(FloatingObject):
    """ A hunk of space rock (in addition to other elements) that try to make the player's ship have a bad day.
    
        Stereotypes:
            Information Holder
        
        Attributes:
            NONE
    """

    def update(self):
        """ Handles what happens on update
        
            Args:
                self (Asteroid): An instance of Asteroid.
        """