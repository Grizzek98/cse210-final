from arcade.sprite_list.sprite_list import SpriteList
from game.enemy.asteroid import Asteroid
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
        asteroid = Asteroid(constants.ASTEROID_SPRITE_DIRECTORY, constants.SPRITE_SCALING)
        start_side = random.randint(1, 4)
        self._get_random_start(start_side, asteroid)
        asteroid.damage = 50
        asteroid.change_angle = self._get_random_rotation()
        asteroid.score_given = 1
        return asteroid

    def _get_random_start(self, start_side, asteroid):
        """ Handles getting a random starting position and velocity for asteroid.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
                start_side (int): The side of the screen to start the object on.
        """
        if start_side == 1:
            self._random_left_start(asteroid)
        elif start_side == 2:
            self._random_right_start(asteroid)
        elif start_side == 3:
            self._random_top_start(asteroid)
        elif start_side == 4:
            self._random_bottom_start(asteroid)

    def _random_left_start(self, asteroid):
        """ Sets a random position and velocity for object on left side of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        asteroid.center_x = -5
        asteroid.center_y = random.randint(0, constants.SCREEN_HEIGHT - 1)
        asteroid.change_x = random.randint(1, constants.ASTEROID_MAX_VELOCITY)
        asteroid.change_y = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)

    def _random_right_start(self, asteroid):
        """ Sets a random position and velocity for object on right side of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        asteroid.center_x = constants.SCREEN_WIDTH + 5
        asteroid.center_y = random.randint(0, constants.SCREEN_HEIGHT)
        asteroid.change_x = random.randint(-constants.ASTEROID_MAX_VELOCITY, -1)
        asteroid.change_y = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)

    def _random_top_start(self, asteroid):
        """ Sets a random position and velocity for object on top of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        asteroid.center_x = random.randint(0, constants.SCREEN_WIDTH)
        asteroid.center_y = constants.SCREEN_HEIGHT + 5
        asteroid.change_x = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)
        asteroid.change_y = random.randint(-constants.ASTEROID_MAX_VELOCITY, -1)

    def _random_bottom_start(self, asteroid):
        """ Sets a random position and velocity for object on bottom of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        asteroid.center_x = random.randint(0, constants.SCREEN_WIDTH)
        asteroid.center_y = -5
        asteroid.change_x = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)
        asteroid.change_y = random.randint(1, constants.ASTEROID_MAX_VELOCITY)

    def _get_random_rotation(self):
        """ Returns a random rotation value.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        return random.randint(-10, 10)