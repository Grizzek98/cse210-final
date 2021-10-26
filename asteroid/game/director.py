
import arcade, random
from os import path

from pyglet.media import player




# from arcade import sprite_list
# from game import player_ship
from game import spawn
from game import constants
from game.player_ship import PlayerShip
from game.asteroid import Asteroid
from game.keyboard_control import KeyboardControl
from game.score import Score
from game.script import GameScript
from game.collision import Collision
from game.score import Score
from game.power_ups import PowerUp
from game.spawn.spawn_power import SpawnPower
from game.enemy_service import EnemyService



class Director(arcade.View):
    """ The main controller class. Handles the flow of the program.
    
        Stereotypes:
            Controller
        
        Attributes:
            sprite_list (list): A list of sprites on-screen.
            asteroid_list (list): A list of asteroid sprites on-screen.
            player_ship (arcade.Sprite): A player_controlled ship sprite object.
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
        # self.sprite_list = None
        # self.asteroid_list = None
        self.player_ship = None
        self.projectile_sprite = None
        self.keyboard_control = KeyboardControl()
        self.player_projectile_list = None
        self.enemy_projectile_list = None
        self.power_list = None
        self.shot_sound = arcade.load_sound(constants.SHOT_SOUND)
        self.spawn_player = spawn.SpawnPlayer()
        # self.spawn_enemy = spawn.SpawnEnemy()
        self.spawn_asteroid = spawn.SpawnAsteroid()
        self.spawn_power = SpawnPower()
        self.power_up = PowerUp()
        self.enemy_service = EnemyService()
        
        self.script = GameScript()
        self.collision = Collision()
        self.score_class = Score()
        self.score = ""
        self.shot_control = 0
        self.fire_rate = constants.PLAYER_FIRERATE
        
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
        # self.asteroid_list = arcade.SpriteList()
        self.power_list = arcade.SpriteList()

        self.player_ship = self.spawn_player.spawn()
        self.sprite_list.append(self.player_ship)
        self.enemy_service.asteroid_list.extend(self.spawn_asteroid.setup())
        self.power_list.append(self.spawn_power.setup(constants.DOUBLEX_POWER_SPRITE))
        

        # self.asteroid = self.spawn_asteroid.spawn()
        # self.asteroid_list.append(self.asteroid)

        # self.shot_sound = arcade.load_sound(path.join(constants.RESOURCE_DIRECTORY, path.join("ST", "laser_shot_effect.mp3")))

    def check_fire(self, delta_time, ship):
        """check if an object is firing this turn"""
        pass

    def on_update(self, delta_time):
        """ Handles what happens every arcade update.
        
            Args:
                self (Director): An instance of Director.
                delta_time (Float): Describes the elapsed time between frames.
        """


        #should spawn
        # if len(self.asteroid_list) < self.script.enemy_max :
        #     self.asteroid_list.append(self.spawn_asteroid.spawn())
        self.script.update(delta_time)

        # call sprite on_update() methods
        self.player_projectile_list.on_update(delta_time)
        self.sprite_list.on_update(delta_time) #<3 arcade
        self.enemy_projectile_list.extend(self.enemy_service.on_update(self.script, delta_time))
        self.score_class.add_score(self.enemy_service.add_score)
        self.power_list.on_update(delta_time)

        self.check_collision()
        self.check_remove_sprite()

        #generate shots
        if self.player_ship.can_fire() :
            self.player_projectile_list.append(self.player_ship.create_shot())
        #Spawn randomly asteroids
        # self.spawn_asteroid_control += delta_time
        # if self.spawn_asteroid_control >= self.asteroid_spawn_rate:
        #     self.asteroid_list.append(self.spawn_asteroid.spawn())
        #     self.spawn_asteroid_control = 0

        #     if self.asteroid_spawn_rate > constants.MAX_SPAWN_RATE:
        #         self.asteroid_spawn_rate -= 0.05
        #     else:
        #         self.asteroid_spawn_rate = constants.MAX_SPAWN_RATE
        

        #Spawn randomly Power Ups
        control = random.random()
        if control < 0.001 and len(self.power_list) < 2 and self.collision.power_up_status == False:
            self.power_list.append(self.spawn_power.spawn(constants.DOUBLEX_POWER_SPRITE))
        
        if self.collision.power_up_status:
            self.power_up.power_up_timer -= delta_time
            self.fire_rate = self.power_up.shot_speed_power()
            
            
            if self.power_up.power_up_timer <= 0:
                 self.fire_rate = constants.PLAYER_FIRERATE
                 self.collision.power_up_status = False
                 self.power_up.timer_reset()
        

        self.score_class.update_highscore()


    def on_draw(self):
        """ Handles what happens every time the screen is refreshed.
        
            Args:
                self (Director): An instance of Director.
        """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        #draws score on screen
        arcade.draw_text(f"Score: {self.score_class.get_score()}", 650, 550, arcade.color.GOLDEN_YELLOW, 10)
        arcade.draw_text(f"Best: {self.score_class.get_highscore()}", 100, 550, arcade.color.GOLDEN_YELLOW, 10)
        if self.collision.power_up_status:
            arcade.draw_text(f"POWER UP: {self.power_up.power_up_timer:.0f}",50, 50, arcade.color.GRAY, 10)
        self.sprite_list.draw()
        self.enemy_service.asteroid_list.draw() 
        self.player_projectile_list.draw()
        self.enemy_projectile_list.draw()
        self.power_list.draw()
        


    def on_key_press(self, key, modifiers):
        """ Handles what happens when a key is pressed.
        
            Args:
                self (ArcadeDirector): An instance of ArcadeDirector.
                key (input): A key pressed by the user.
                BUG modifiers (not sure): Haven't quite learned what the modifiers could be.
        """
        self.keyboard_control.key_press(key, self.player_ship)  


    def on_key_release(self, key, modifiers):
        """ Handles what happens when a key is released.
        
            Args:
                self (ArcadeDirector): An instance of ArcadeDirector.
                key (input): A key pressed by the user.
                BUG modifiers (not sure): Haven't quite learned what the modifiers could be.
        """
        self.keyboard_control.key_release(key, self.player_ship)

    def check_collision(self):
        """ Checks for collision between objects on the screen.
        
            Args:
                self (Director): An instance of Director.
        """

        self.collision.check_collision(self.player_ship, self.enemy_service.asteroid_list,
            self.player_projectile_list, self.enemy_projectile_list, self.power_list)

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
        ## remove dead stuff

        # remove dead player
        for sprite in self.sprite_list:
            if sprite.get_hit_points() <= 0:
                self.sprite_list.remove(sprite)

        # remove dead asteroids


        ## remove out-of-bounds stuff

        # remove gone asteroids

        # remove gone player_projectiles
        for sprite in self.player_projectile_list:
            if sprite.check_bounds_x() or sprite.check_bounds_y():
                self.player_projectile_list.remove(sprite)

        # remove gone enemy_projectiles
        for sprite in self.enemy_projectile_list:
            if sprite.check_bounds_x() or sprite.check_bounds_y():
                self.enemy_projectile_list.remove(sprite)