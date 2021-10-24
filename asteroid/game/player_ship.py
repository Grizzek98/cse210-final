
from game import constants
from game.floating_object import FloatingObject
import game.weapon

class PlayerShip(FloatingObject):
    """ A player-controlled ship that moves around the screen.
    
        Stereotypes:
            Information Holder
        
        Attributes:
            is_shooting (Bool), indictes if the ship is currently firing or not.
            target_angle (float), the direction the ship is rotating towards. None if ship is not rotating
    """
    def __init__(self, filename= constants.SHIP_SPRITE_DIRECTORY, scale= constants.SPRITE_SCALING):
        super().__init__(filename= filename, scale= scale)
        self.is_shooting = False
        self.weapon = game.weapon.BasicLaser() #default
        self.power_up = None #TODO unimplemented powerup field
        
    def on_update(self, delta_time):
        """ Handles what happens on update
        
            Args:
                self (PlayerShip): An instance of PlayerShip.
        """
        if not self._check_change_x():
            self._accelerate_x()
            pass

        if not self._check_change_y():
            self._accelerate_y()
            pass
        self._rectify_angle()
        self._check_angle()
        self.rotate()
        self.move_x()
        self.move_y()
        self._check_velocity_bounds()
        self.check_bounds_x()
        self.check_bounds_y()
        self._update_weapon(delta_time)
    
    def can_fire(self):
        """check if the ship can fire a shot
        args:
            self (PlayerShip) an instance of PlayerShip"""
        if self.is_shooting:
            return self.weapon.can_fire()
        else :
            return False

    def create_shot(self) -> game.weapon.Projectile:
        """request and return a shot from the current weapon
            args:
                self (PlayerShip) an instance of PlayerShip"""
        return self.weapon.generate_shot(self)

    def _update_weapon(self, delta_time):
        """call the weapon's on_update method
        args:
            self (PlayerShip) an instance of PlayerShip
            delta_time (float) time since last frame
            """
        self.weapon.on_update(delta_time)

    def check_bounds_x(self):
        """ Checks whether object has reached the x boundary.
        
            Args:
                self (PlayerShip): An instance of PlayerShip.
        """
        if self.left < 0:
            self.left = 0
        if self.right > constants.SCREEN_WIDTH - 1:
            self.right = constants.SCREEN_WIDTH

    def check_bounds_y(self):
        """ Checks whether object has reached the y boundary.
        
            Args:
                self (PlayerShip): An instance of PlayerShip.
        """
        if self.bottom < 0:
            self.bottom = 0
        if self.top > constants.SCREEN_HEIGHT - 1:
            self.top = constants.SCREEN_HEIGHT