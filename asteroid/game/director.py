
import arcade
from os import path

from pyglet.media import player

# from arcade import sprite_list
# from game import player_ship

from game import constants
from game.player_ship import PlayerShip
from game.asteroid import Asteroid
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
        self.player_projectile_list = None
        self.enemy_projectile_list = None
        self.shot_sound = arcade.load_sound(path.join(constants.RESOURCE_DIRECTORY, path.join("ST", "laser_shot_effect.mp3")))

    def setup(self):
        """ Handles the initial setup of the game.
        
            Args:
                self (Director): An instance of Director.
        """
        self.sprite_list = arcade.SpriteList()
        self.player_projectile_list = arcade.SpriteList()
        self.enemy_projectile_list = arcade.SpriteList()
        self.asteroid_sprite_list = arcade.SpriteList()

        self.player_ship_sprite = PlayerShip(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "player_ship.png")), constants.SPRITE_SCALING)
        self.player_ship_sprite.center_x = constants.SCREEN_WIDTH / 2
        self.player_ship_sprite.center_y = constants.SCREEN_HEIGHT / 2
        self.player_ship_sprite.hit_points = 100
        self.sprite_list.append(self.player_ship_sprite)

        self.asteroid_sprite = Asteroid(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "asteroid.png")), constants.SPRITE_SCALING)
        self.asteroid_sprite.center_x = constants.SCREEN_WIDTH / 2 + 100
        self.asteroid_sprite.center_y = constants.SCREEN_HEIGHT / 2 + 100
        self.asteroid_sprite.damage = 50
        self.asteroid_sprite_list.append(self.asteroid_sprite)

        # self.shot_sound = arcade.load_sound(path.join(constants.RESOURCE_DIRECTORY, path.join("ST", "laser_shot_effect.mp3")))

    def on_update(self, delta_time):
        """ Handles what happens every update.
        
            Args:
                self (Director): An instance of Director.
                delta_time (not sure): Describes the elapsed time between frames.
        """
        if self.player_ship_sprite.is_shooting:
            new_shot = Projectile(self.player_ship_sprite.center_x, self.player_ship_sprite.center_y,
            self.player_ship_sprite.angle)
            self.player_projectile_list.append(new_shot)
            self.play_shoot_sound()
            pass
        self.player_projectile_list.update()
        self.check_collision()
        self.sprite_list.update() #TODO can't pass in delta_time like this. 
        self.check_remove_sprite()

    def on_draw(self):
        """ Handles what happens every time the screen is refreshed.
        
            Args:
                self (Director): An instance of Director.
        """
        arcade.start_render()
        self.sprite_list.draw()
        self.asteroid_sprite_list.draw()
        self.player_projectile_list.draw()
        self.enemy_projectile_list.draw()


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
    
    def shot(self): #TODO create constructor returning new shots
        """Creates a projectile

        Args:
            self (Director): An instance of Director.
    """
        self.projectile_sprite = Projectile(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "projectile.png")), constants.SPRITE_SCALING)
        self.projectile_sprite.center_x = self.player_ship_sprite.center_x
        self.projectile_sprite.center_y = self.player_ship_sprite.center_y - 100
        self.player_projectile_list.append(self.projectile_sprite)
        
    def check_collision(self):
        """ Checks for collision between objects on the screen.
        
            Args:
                self (Director): An instance of Director.
        """
        # player - asteroids
        for asteroid in arcade.check_for_collision_with_list(self.player_ship_sprite, self.asteroid_sprite_list):
            self.player_ship_sprite.subtract_hit_points(asteroid.damage)
        # player - enemy projectiles
        for projectile in arcade.check_for_collision_with_list(self.player_ship_sprite, self.enemy_projectile_list):
            self.player_ship_sprite.subtract_hit_points(projectile.damage)
            self.enemy_projectile_list.remove(projectile)
        # player projectiles - asteroids
        for projectile in self.player_projectile_list:
            for asteroid in arcade.check_for_collision_with_list(projectile, self.asteroid_sprite_list):
                asteroid.subtract_hit_points(projectile.damage)
                self.player_projectile_list.remove(projectile)
        # player projectiles - enemy pro
        for player_projectile in self.player_projectile_list:
            for enemy_projectile in arcade.check_for_collision_with_list(player_projectile, self.enemy_projectile_list):
                self.enemy_projectile_list.remove(enemy_projectile)
                self.player_projectile_list.remove(player_projectile)
        # 
        # 
        # jectiles

    def play_shoot_sound(self):
            """ Plays the shot sound effect when the player shoots

                Args:
                    self (Director): An instance of Director.
            """
            arcade.play_sound(self.shot_sound)

    def check_remove_sprite(self):
        """ Checks whether a sprite should be remove from screen based on hit points.
        
            Args:
                self (Director): An instance of Director.
        """
        # remove dead player
        for sprite in self.sprite_list:
            if sprite.get_hit_points() <= 0:
                self.sprite_list.remove(sprite)

        # remove dead asteroids
        for sprite in self.asteroid_sprite_list:
            if sprite.get_hit_points() <= 0:
                self.asteroid_sprite_list.remove(sprite)