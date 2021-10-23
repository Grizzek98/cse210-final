from arcade.sprite_list.sprite_list import SpriteList
from game.power_ups import PowerUp
from game import constants
import random
import arcade


class SpawnPower:
    """ Handles the spawning of power up objects. 
    
        Stereotypes:
            Information Holder
            Service Provider
        
        Attributes:
            NONE
    """

    def __init__(self):
        """ The class constructor.
        
            Args:
                self (SpawnPower): An instance of SpawnPower.
        """
        self._power_up_list = None

    def setup(setup, sprite):
        """Spawns a power up sprite off bound to avoid the initial lag when the first power up is created (Need to find a better way to do this)"""
        power_up = PowerUp(sprite, constants.SPRITE_SCALING)
        power_up.center_x = constants.SCREEN_WIDTH + 15
        power_up.center_y = constants.SCREEN_HEIGHT + 15
        return power_up

    def spawn(self, sprite):
        """ Instantiates a power up object.
        
            Args:
                self (SpawnPower): An instance of SpawnPower.
        """
        self.power_up = PowerUp(sprite, constants.SPRITE_SCALING)
        self._get_random_start()
        return self.power_up


    def _get_power_up(self):
        """Chooses the power up to be spawn

            Args:
                TODO
        """
        power_up = random.choice(self.power_up_list)

    def _get_random_start(self):
        """ Handles getting a random starting position the power up.
        
            Args:
                self (SpawnPowerUp): An instance of SpawnPowerUp.
        """
        self.power_up.center_x = random.randint(0 , constants.SCREEN_WIDTH)
        self.power_up.center_y = random.randint(0 , constants.SCREEN_HEIGHT)

   