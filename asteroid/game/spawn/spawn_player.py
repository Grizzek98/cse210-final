from game.player_ship import PlayerShip
from game import constants

class SpawnPlayer:
    """ Handles the spawning of the player's ship object.
    
        Stereotypes:
            Information Holder
            Service Provider
        
        Attributes:
            NONE
    """

    def __init__(self):
        """ The class constructor.
        
            Args:
                self (SpawnPlayer): An instance of SpawnPlayer.
        """

    def spawn(self):
        """ Handles game initialization for the player object.
        
            Args:
                self (SpawnPlayer): An instance of SpawnPlayer.
        """
        self.player_ship = PlayerShip(constants.SHIP_SPRITE_DIRECTORY, constants.SPRITE_SCALING)
        self.player_ship.center_x = constants.SCREEN_WIDTH / 2
        self.player_ship.center_y = constants.SCREEN_HEIGHT / 2
        self.player_ship.hit_points = 100
        return self.player_ship