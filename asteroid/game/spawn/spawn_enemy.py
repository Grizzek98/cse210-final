
from arcade.sprite_list.sprite_list import SpriteList
from game.enemy.enemy_ship import EnemyShip
from game import constants
import random
import arcade

class SpawnEnemy:
    """ Handles the spawning of enemy ship objects.
    
        Stereotypes:
            Information Holder
            Service Provider
        
        Attributes:
            NONE
    """

    def setup(self):
        """ Handles game initialization for the enemy object.
        
            Args:
                self (SpawnEnemy): An instance of SpawnEnemy.
        """
        pass

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
        self.asteroid.change_x = random.randint(1, constants.ASTEROID_MAX_VELOCITY)
        self.asteroid.change_y = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)

    def _random_right_start(self):
        """ Sets a random position and velocity for object on right side of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self.asteroid.center_x = constants.SCREEN_WIDTH + 5
        self.asteroid.center_y = random.randint(0, constants.SCREEN_HEIGHT)
        self.asteroid.change_x = random.randint(-constants.ASTEROID_MAX_VELOCITY, -1)
        self.asteroid.change_y = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)

    def _random_top_start(self):
        """ Sets a random position and velocity for object on top of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self.asteroid.center_x = random.randint(0, constants.SCREEN_WIDTH)
        self.asteroid.center_y = constants.SCREEN_HEIGHT + 5
        self.asteroid.change_x = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)
        self.asteroid.change_y = random.randint(-constants.ASTEROID_MAX_VELOCITY, -1)

    def _random_bottom_start(self):
        """ Sets a random position and velocity for object on bottom of screen.
        
            Args:
                self (SpawnAsteroid): An instance of SpawnAsteroid.
        """
        self.asteroid.center_x = random.randint(0, constants.SCREEN_WIDTH)
        self.asteroid.center_y = -5
        self.asteroid.change_x = random.randint(-constants.ASTEROID_MAX_VELOCITY, constants.ASTEROID_MAX_VELOCITY)
        self.asteroid.change_y = random.randint(1, constants.ASTEROID_MAX_VELOCITY)
