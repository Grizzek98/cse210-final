from arcade.sprite import Sprite
from game.floating_object import FloatingObject
from game.weapon.weapons import Weapons
from game.weapon.projectile import Projectile


class BasicLaser(Weapons):
    """ A basic burst laser weapon.

        Stereotypes:
            Information Holder

        Attributes:
            TODO
    """

    def __init__(self):
        super().__init__()
        """ Instantiates an instance of BasicLaser.
        
            Args:
                self (BasicLaser): An instance of BasicLaser.
        """
        self.fire_rate = 0