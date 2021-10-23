import arcade
from game.score import Score

class Collision:
    """ Handles collision logic between sprites on the screen.
    
        Stereotypes:
            Service Provider
        
        Attributes:
            TODO
    """

    def __init__(self):
        """ The class constructor.
        
            Args:
                self (Collision): An instance of Collision.
        """
        self.score = Score()
        self.power_up_status = False

    def check_collision(self, player_ship=None, asteroid_list=None, player_projectile_list=None,
                        enemy_projectile_list=None, power_up_list = None):
        """ Handles checking for collision, received lists, modifies them.
        
            Args:
                self (Collision): An instance of Collision.
        """
        self.check_player_collision(player_ship, asteroid_list, enemy_projectile_list, power_up_list)
        self.check_player_projectile_collision(player_projectile_list, asteroid_list, enemy_projectile_list)

    def check_player_collision(self, player_ship, asteroid_list, enemy_projectile_list, power_up_list):
        """ Checks whether the player_ship has collided with anything.
        
            Args: 
                self (Collision): An instance of Collision.
        """
        #player - asteroid
        for asteroid in arcade.check_for_collision_with_list(player_ship, asteroid_list):
            player_ship.subtract_hit_points(asteroid.damage)
        #player - enemy projectile
        for projectile in arcade.check_for_collision_with_list(player_ship, enemy_projectile_list):
            player_ship.subtract_hit_points(projectile.damage)
            enemy_projectile_list.remove(projectile)
        #player - power up
        for power_up in arcade.check_for_collision_with_list(player_ship, power_up_list):
            self.power_up_status = True            
            power_up_list.remove(power_up)
            


    def check_player_projectile_collision(self, player_projectile_list, asteroid_list,
            enemy_projectile_list):
        """ Checks whether the player's projectiles have collided with anything.
        
            Args:
                self (Collision): An instance of Collision.
        """
        #player_projectile - asteroid
        for projectile in player_projectile_list:
            for asteroid in arcade.check_for_collision_with_list(projectile, asteroid_list):
                asteroid.subtract_hit_points(projectile.damage)
                try:
                    player_projectile_list.remove(projectile)
                except:
                    pass
                self.score.add_score(asteroid.get_score_given())
        #player_projectile - enemy_projectile
        for player_projectile in player_projectile_list:
            for enemy_projectile in arcade.check_for_collision_with_list(player_projectile, enemy_projectile_list):
                enemy_projectile_list.remove(enemy_projectile)
                player_projectile_list.remove(player_projectile)
