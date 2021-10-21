
import arcade
from os import path

from pyglet.media import player


# from arcade import sprite_list
# from game import player_ship
from game import spawn
from game import constants
from game.player_ship import PlayerShip
from game.asteroid import Asteroid
from game.keyboard_control import KeyboardControl
from game.projectile import Projectile
from game.score import Score


class Director(arcade.View):
    """ The main controller class. Handles the flow of the program.
    
        Stereotypes:
            Controller
        
        Attributes:
            sprite_list (list): A list of sprites on-screen.
            asteroid_list (list): A list of asteroid sprites on-screen.
            player_ship_sprite (arcade.Sprite): A player_controlled ship sprite object.
            asteroid (arcade.Sprite): An asteroid sprite object.
            projectile_sprite (arcade.Sprite): An instance of a projectile on-screen.
            keyboard_control (KeyboardControl): An instance of KeyboardControl.
    """

    def __init__(self):
        """ The constructor of the class. Initializes the classes attributes and opens the arcade window.
        
            Args:
                self (Director): An instance of Director.
                width (constant): The width of the arcade screen.
                height (constant): The height of the arcade screen.
                title (constant): The title of the arcade screen.
        """
        super().__init__()
        self.window.set_mouse_visible(False)
        self.texture = arcade.load_texture(constants.SPACE_BG)
        self.sprite_list = None
        self.asteroid_list = None
        self.player_ship_sprite = None
        self.projectile_sprite = None
        self.keyboard_control = KeyboardControl()
        self.player_projectile_list = None
        self.enemy_projectile_list = None
        self.shot_sound = arcade.load_sound(constants.SHOT_SOUND)
        self.spawn_player = spawn.SpawnPlayer()
        self.spawn_enemy = spawn.SpawnEnemy()
        self.spawn_asteroid = spawn.SpawnAsteroid()
        self.score = Score()
        self.spawn_asteroid_control = 0
        self.asteroid_spawn_rate = 1

    def setup(self):
        """ Handles the initial setup of the game.
        
            Args:
                self (Director): An instance of Director.
        """
        self.sprite_list = arcade.SpriteList()
        self.player_projectile_list = arcade.SpriteList()
        self.enemy_projectile_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

        self.player_ship_sprite = self.spawn_player.spawn()
        self.sprite_list.append(self.player_ship_sprite)
        self.asteroid_list.extend(self.spawn_asteroid.setup())

        # self.asteroid = self.spawn_asteroid.spawn()
        # self.asteroid_list.append(self.asteroid)

        # self.shot_sound = arcade.load_sound(path.join(constants.RESOURCE_DIRECTORY, path.join("ST", "laser_shot_effect.mp3")))

    def on_update(self, delta_time):
        """ Handles what happens every arcade update.
        
            Args:
                self (Director): An instance of Director.
                delta_time (not sure): Describes the elapsed time between frames.
        """
        if self.player_ship_sprite.is_shooting:
            new_shot = Projectile(self.player_ship_sprite.center_x, self.player_ship_sprite.center_y,
            self.player_ship_sprite.angle)
            self.player_projectile_list.append(new_shot)
            self.play_shoot_sound()
        self.player_projectile_list.on_update(delta_time)
        self.sprite_list.on_update(delta_time) #<3 arcade
        self.asteroid_list.on_update(delta_time)
        self.check_collision()
        self.check_remove_sprite()

        #Spawn randomly asteroids
        self.spawn_asteroid_control += delta_time
        if self.spawn_asteroid_control >= self.asteroid_spawn_rate:
            self.asteroid_list.append(self.spawn_asteroid.spawn())
            self.spawn_asteroid_control = 0

            if self.asteroid_spawn_rate > constants.MAX_SPAWN_RATE:
                self.asteroid_spawn_rate -= 0.05
            else:
                self.asteroid_spawn_rate = constants.MAX_SPAWN_RATE


    def on_draw(self):
        """ Handles what happens every time the screen is refreshed.
        
            Args:
                self (Director): An instance of Director.
        """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.sprite_list.draw()
        self.asteroid_list.draw()
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
        for asteroid in arcade.check_for_collision_with_list(self.player_ship_sprite, self.asteroid_list):
            self.player_ship_sprite.subtract_hit_points(asteroid.damage)
        # player - enemy projectiles
        for projectile in arcade.check_for_collision_with_list(self.player_ship_sprite, self.enemy_projectile_list):
            self.player_ship_sprite.subtract_hit_points(projectile.damage)
            self.enemy_projectile_list.remove(projectile)
        # player projectiles - asteroids
        for projectile in self.player_projectile_list:
            for asteroid in arcade.check_for_collision_with_list(projectile, self.asteroid_list):
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
        ## remoce dead stuff

        # remove dead player
        for sprite in self.sprite_list:
            if sprite.get_hit_points() <= 0:
                self.sprite_list.remove(sprite)

        # remove dead asteroids
        for sprite in self.asteroid_list:
            if sprite.get_hit_points() <= 0:
                self.asteroid_list.remove(sprite)

        ## remove out-of-bounds stuff

        # remove gone asteroids
        for sprite in self.asteroid_list:
            if sprite.check_bounds_x() or sprite.check_bounds_y():
                self.asteroid_list.remove(sprite)

        # remove gone player_projectiles
        for sprite in self.player_projectile_list:
            if sprite.check_bounds_x() or sprite.check_bounds_y():
                self.player_projectile_list.remove(sprite)

        # remove gone enemy_projectiles
        for sprite in self.enemy_projectile_list:
            if sprite.check_bounds_x() or sprite.check_bounds_y():
                self.enemy_projectile_list.remove(sprite)