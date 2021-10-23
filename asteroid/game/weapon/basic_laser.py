from arcade.sprite import Sprite
from game.floating_object import FloatingObject
from weapon import Weapon
from projectile import Projectile


class BasicLaser(Weapon):
    """ A basic burst laser weapon.

        Stereotypes:
            Information Holder

        Attributes:
            TODO
    """

    def __init__(self):
        """ Instantiates an instance of BasicLaser.
        
            Args:
                self (BasicLaser): An instance of BasicLaser.
        """
        self.projectile_sprite = Projectile
    
    def generate_shot(self, ship: Sprite) -> Projectile:
        """Returns a projectile with correct positon and orientation
        args: ship (Sprite) the object 'creating' the shot"""
        return self.projectile_sprite(center_x= ship.center_x,center_y = ship.center_y, angle= ship.angle)