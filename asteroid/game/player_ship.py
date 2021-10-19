
from game import constants
from game.floating_object import FloatingObject

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

        #used to indicate a turn stop
        self.target_angle = 0

        #used for smooth accel/decceleration
        self.target_change_x = 0
        self.target_change_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0


    def _rectify_angle(self):
        """checks to make sure angle is between 0 inclusive and 360 exclusive
        and alters angle if needed."""
        if self.angle == 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360 + self.angle
        pass

    def _check_angle(self):
        """checks if current angle has reached target angle and
        updates change_angle and if needed
        """
        if self.target_angle == self.angle :
            self.target_angle = None #BUG probably target angle doesn't need to change
            self.change_angle = 0

    def _check_change_x(self):
        """checks if x velocity has reached target and
        returns True if x vel == target"""
        # if self.change_x > constants.MOVEMENT_SPEED :
        #     self.change_x = constants.MOVEMENT_SPEED
        # elif self.change_x < -constants.MOVEMENT_SPEED :
        #     self.change_x = -constants.MOVEMENT_SPEED
        if self.target_change_x == self.change_x :
            return True
        else :
            return False

    def _check_change_y(self):
        """checks if y velocity has reached target.
        returns True if x vel == target"""
        # if self.change_y > constants.MOVEMENT_SPEED :
        #     self.change_y = constants.MOVEMENT_SPEED
        # elif self.change_y < -constants.MOVEMENT_SPEED :
        #     self.change_y = -constants.MOVEMENT_SPEED
        if self.target_change_y == self.change_y :
            return True
        else :
            return False

    def _check_velocity_bounds(self):
        """check if velocity is out of bounds (greater than max)
        set velocity to max if it is out of bounds"""
        pass

    def _accelerate_x(self):
        """add accel x to change x"""
        self.change_x += self.acceleration_x
    
    def _accelerate_y(self):
        """add accel y to change y"""
        self.change_y += self.acceleration_y

    def update(self):
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