
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
        pass
    
    def on_hit(self):
        """Subtracts HP"""
        
        self.hit_points = self.hit_points - 1
        return self.hit_points


class SimpleAsteroid(Asteroid):
    """"""
    hit_points = 1

    def get_hit_points(self):
       
       return self.hit_points

    def on_hit(self):
        self.hit_points = self.hit_points - 1