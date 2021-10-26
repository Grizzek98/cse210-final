
import game.weapon
from game.floating_object import FloatingObject

class EnemyShip(FloatingObject):
    """ A basic enemy ship. Does not like the player.
    
        Stereotypes:
            Information Holder
        
        Attributes:
            TODO
    """

    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture=None, angle: float = 0, hit_points=100, damage=100, score_given=1, acceleration_x=0, acceleration_y=0):
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle, hit_points=hit_points, damage=damage, score_given=score_given, acceleration_x=acceleration_x, acceleration_y=acceleration_y)
        """ The class constructor.
        
            Args:
                All arcade.Sprite params.
        """
        pass

    def on_update(self, delta_time):
        """ Handles what the object does every update.
        
            Args:
                self (EnemyShip): An instance of EnemyShip.
                delta_time (Float): Describes the elapsed time between frames. 
        """
        self.rotate()
        self.move_x()
        self.move_y()
        self.check_bounds_x()
        self.check_bounds_y()
        self._update_weapon(delta_time)

    def create_shot(self) -> game.weapon.Projectile:
        """request and return a shot from the current weapon
            args:
                self (EnemyShip) an instance of EnemyShip"""
        return self.weapon.generate_shot(self)

    def _update_weapon(self, delta_time):
        """call the weapon's on_update method
        args:
            self (EnemyShip) an instance of EnemyShip
            delta_time (float) time since last frame
            """
        self.weapon.on_update(delta_time)
