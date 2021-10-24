from arcade.sprite_list.sprite_list import SpriteList
from game.asteroid import Asteroid
from game import constants
import random
import arcade


class SpawnAsteroid:
    """ Handles the spawning of asteroid objects. TODO add an asteroid max velocity constant TODO
    
        Stereotypes:
            Information Holder
            Service Provider
        
        Attributes:
            NONE
    """

    def __init__(self):
        """ The class constructor.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self._asteroid_list = None

    def setup(self):
        """ Handles setup for asteroids on game setup.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self._asteroid_list = arcade.SpriteList()
        for x in range(random.randint(3, 5)):
            self._asteroid_list.append(self.spawn())
        return self._asteroid_list

    def spawn(self):
        """ Instantiates an asteroid object.
        
            Args:
                self (SpawnEnemy): An instance of SpawnEnemy.
        """
        self.asteroid = Asteroid(constants.ASTEROID_SPRITE_DIRECTORY, constants.SPRITE_SCALING)
        self.start_side = random.randint(1, 4)
        self._get_random_start(self.start_side)
        self.asteroid.damage = 50
        self.asteroid.change_angle = self._get_random_rotation()
        self.asteroid.score_given = 1
        return self.asteroid

    def _get_random_start(self, start_side):
        """ Handles getting a random starting position and velocity for asteroid.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
                start_side (int): The side of the screen to start the object on.
        """
        if start_side == 1:
            self._random_left_start()
        elif start_side == 2:
            self._random_right_start()
        elif start_side == 3:
            self._random_top_start()
        elif start_side == 4:
            self._random_bottom_start()

    def _random_left_start(self):
        """ Sets a random position and velocity for object on left side of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self.asteroid.center_x = -5
        self.asteroid.center_y = random.randint(0, constants.SCREEN_HEIGHT - 1)
        self.asteroid.change_x = random.randint(1, 5)
        self.asteroid.change_y = random.randint(-5, 5)

    def _random_right_start(self):
        """ Sets a random position and velocity for object on right side of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self.asteroid.center_x = constants.SCREEN_WIDTH + 5
        self.asteroid.center_y = random.randint(0, constants.SCREEN_HEIGHT)
        self.asteroid.change_x = random.randint(-5, -1)
        self.asteroid.change_y = random.randint(-5, 5)

    def _random_top_start(self):
        """ Sets a random position and velocity for object on top of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self.asteroid.center_x = random.randint(0, constants.SCREEN_WIDTH)
        self.asteroid.center_y = constants.SCREEN_HEIGHT + 5
        self.asteroid.change_x = random.randint(-5, 5)
        self.asteroid.change_y = random.randint(-5, -1)

    def _random_bottom_start(self):
        """ Sets a random position and velocity for object on bottom of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self.asteroid.center_x = random.randint(0, constants.SCREEN_WIDTH)
        self.asteroid.center_y = -5
        self.asteroid.change_x = random.randint(-5, 5)
        self.asteroid.change_y = random.randint(1, 5)

    def _get_random_rotation(self):
        """ Returns a random rotation value.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        return random.randint(-10, 10)