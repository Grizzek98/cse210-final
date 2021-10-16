
import arcade
from os import path

from game import constants
from game.player_ship import PlayerShip
from game.asteroid import Asteroid
from game.keyboard_control import KeyboardControl

class Director(arcade.Window):
    """ The main controller class. Handles the flow of the program.
    
        Stereotypes:
            Controller
        
        Attributes:
            sprite_list (list): A list of sprites on-screen.
            player_ship_sprite (arcade.Sprite): A player_controlled ship sprite object.
            asteroid (arcade.Sprite): An asteroid sprite object.
    """

    def __init__(self, width, height, title):
        """ The constructor of the class. Initializes the classes attributes and opens the arcade window.
        
            Args:
                self (Director): An instance of Director.
                width (constant): The width of the arcade screen.
                height (constant): The height of the arcade screen.
                title (constant): The title of the arcade screen.
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLUE_GREEN)
        self.sprite_list = None
        self.player_ship_sprite = None
        self.asteroid_sprite = None
        self.keyboard_control = KeyboardControl()

    def setup(self):
        """ Handles the initial setup of the game.
        
            Args:
                self (Director): An instance of Director.
        """
        self.sprite_list = arcade.SpriteList()

        self.player_ship_sprite = PlayerShip(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "player_ship.jpg")), constants.SPRITE_SCALING)
        self.player_ship_sprite.center_x = constants.SCREEN_WIDTH / 2
        self.player_ship_sprite.center_y = constants.SCREEN_HEIGHT / 2
        self.sprite_list.append(self.player_ship_sprite)

    def on_update(self, delta_time):
        """ Handles what happens every update.
        
            Args:
                self (Director): An instance of Director.
                delta_time (not sure): Describes the elapsed time between frames.
        """
        self.sprite_list.update()

    def on_draw(self):
        """ Handles what happens every time the screen is refreshed.
        
            Args:
                TODO
        """
        arcade.start_render()
        self.sprite_list.draw()


    def on_key_press(self, key, modifiers):
        """ Handles what happens when a key is pressed.
        
            Args:
                self (ArcadeDirector): An instance of ArcadeDirector.
                key (input): A key pressed by the user.
                BUG modifiers (not sure): Haven't quite learned what the modifiers could be.
        """
        self.player_ship_sprite.key_press(key)

    def on_key_release(self, key, modifiers):
        """ Handles what happens when a key is released.
        
            Args:
                self (ArcadeDirector): An instance of ArcadeDirector.
                key (input): A key pressed by the user.
                BUG modifiers (not sure): Haven't quite learned what the modifiers could be.
        """
        self.player_ship_sprite.key_release(key)

    def check_collision(self):
        """ Checks for collision between objects on the screen.
        
            Args:
                TODO
        """
        pass