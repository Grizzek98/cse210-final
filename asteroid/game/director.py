
import arcade
from os import path
from game import player_ship

# from arcade import sprite_list
# from game import player_ship

from game import constants
from game.player_ship import PlayerShip
from game.asteroid import *
from game.keyboard_control import KeyboardControl
from game.projectile import Projectile


class Director(arcade.Window):
    """ The main controller class. Handles the flow of the program.
    
        Stereotypes:
            Controller
        
        Attributes:
            sprite_list (list): A list of sprites on-screen.
            asteroid_sprite_list (list): A list of asteroid sprites on-screen.
            player_ship_sprite (arcade.Sprite): A player_controlled ship sprite object.
            asteroid (arcade.Sprite): An asteroid sprite object.
            projectile_sprite (arcade.Sprite): An instance of a projectile on-screen.
            keyboard_control (KeyboardControl): An instance of KeyboardControl.
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
        self.asteroid_sprite_list = None
        self.player_ship_sprite = None
        self.asteroid_sprite = None
        self.projectile_sprite = None
        self.keyboard_control = KeyboardControl()
        self.projectile_list = None

    def setup(self):
        """ Handles the initial setup of the game.
        
            Args:
                self (Director): An instance of Director.
        """
        self.sprite_list = arcade.SpriteList()
        self.projectile_list = arcade.SpriteList()
        self.asteroid_sprite_list = arcade.SpriteList()

        self.player_ship_sprite = PlayerShip(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "player_ship.png")), constants.SPRITE_SCALING)
        self.player_ship_sprite.center_x = constants.SCREEN_WIDTH / 2
        self.player_ship_sprite.center_y = constants.SCREEN_HEIGHT / 2
        self.sprite_list.append(self.player_ship_sprite)

        self.asteroid_sprite = SimpleAsteroid(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "asteroid.png")), constants.SPRITE_SCALING)
        self.asteroid_sprite.center_x = constants.SCREEN_WIDTH / 2 + 100
        self.asteroid_sprite.center_y = constants.SCREEN_HEIGHT / 2 + 100
        self.asteroid_sprite_list.append(self.asteroid_sprite)

    def on_update(self, delta_time):
        """ Handles what happens every update.
        
            Args:
                self (Director): An instance of Director.
                delta_time (not sure): Describes the elapsed time between frames.
        """
        if self.player_ship_sprite.is_shooting:
            new_shot = Projectile(self.player_ship_sprite.center_x,
            self.player_ship_sprite.center_y,
            self.player_ship_sprite.angle)
            self.projectile_list.append(new_shot)
            pass
        self.projectile_list.update()
        self.sprite_list.update() #<3 arcade
        self.check_collision()

    def on_draw(self):
        """ Handles what happens every time the screen is refreshed.
        
            Args:
                self (Director): An instance of Director.
        """
        arcade.start_render()
        self.sprite_list.draw()
        self.asteroid_sprite_list.draw()
        self.projectile_list.draw()


    def on_key_press(self, key, modifiers):
        """ Handles what happens when a key is pressed.
        
            Args:
                self (ArcadeDirector): An instance of ArcadeDirector.
                key (input): A key pressed by the user.
                BUG modifiers (not sure): Haven't quite learned what the modifiers could be.
        """
        self.keyboard_control.key_press(key, self.player_ship_sprite)  


    def on_key_release(self, key, modifiers):
        """ Handles what happens when a key is released.
        
            Args:
                self (ArcadeDirector): An instance of ArcadeDirector.
                key (input): A key pressed by the user.
                BUG modifiers (not sure): Haven't quite learned what the modifiers could be.
        """
        self.keyboard_control.key_release(key, self.player_ship_sprite)
    
    def shot(self):
        """Creates a projectile

        Args:
            self (Director): An instance of Director.
    """
        self.projectile_sprite = Projectile(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "projectile.png")), constants.SPRITE_SCALING)
        self.projectile_sprite.center_x = self.player_ship_sprite.center_x
        self.projectile_sprite.center_y = self.player_ship_sprite.center_y - 100
        self.projectile_list.append(self.projectile_sprite)
        
    def check_collision(self):
        """ Checks for collision between objects on the screen.
        
            Args:
                self (Director): An instance of Director.
        """
        #Checks the collision between the ship and asteroids (Lose Game)
        if arcade.check_for_collision_with_list(self.player_ship_sprite,self.asteroid_sprite_list):
            self.player_ship_sprite.on_hit()
            if self.player_ship_sprite.get_hit_points() == 0:
                self.remove_from_screen(self.player_ship)
                
                
            
                   
                    
    def remove_from_screen(self, list):
        """ Removes objects from the screen (and sprite_list).
        """
        self.sprite_list.remove(self.player_ship_sprite)

    

