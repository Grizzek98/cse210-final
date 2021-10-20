import arcade
from game import constants

class FloatingObject(arcade.Sprite):
    """ An object on the screen. May or may not move.
    
        Stereotypes:
            Information Holder
        
        Attributes:
   
    """
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture = None, angle: float = 0,
    hit_points= 100, damage= 100, acceleration_x= 0, acceleration_y= 0): #non Sprite args
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle)
        """ The class contructor.
        
            Args:
                all arcade.Sprite params
                self (FloatingObject): An instance of FloatingObject.
                hit_points (int) starting HP
                damage (int) damage dealt on contact
                acceleration_x (float) change in x velocity
                acceperation_y (float) change in y velocity

        """
        self.hit_points = hit_points
        self.damage = damage

        #used to indicate a turn stop
        self.target_angle = None
        #used for smooth accel/decceleration
        self.target_change_x = None
        self.target_change_y = None
        self.acceleration_x = 0
        self.acceleration_y = 0

    def on_update(self, delta_time):
        """ Handles what the object does every update.
        
            Args: 
                self (FloatingObject): An instance of FloatingObject.
        """
        self.rotate()
        self.move_x()
        self.move_y()
        self.check_bounds_x()
        self.check_bounds_y()

    def rotate(self):
        """ Rotates the object according to self.change_angle. Assumes degrees
            
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        self.angle += self.change_angle
        
    def move_x(self):
        """ Moves the object along the x axis.
        
            Args: 
                self (FloatingObject): An instance of FloatingObject.
        """
        self.center_x += self.change_x

    def move_y(self):
        """ Moves the object along the y axis.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        self.center_y += self.change_y

    def check_bounds_x(self):
        """ Checks if object is beyond x bounds.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        if self.left < 0 or self.right > constants.SCREEN_WIDTH - 1:
            return True
    
    def check_bounds_y(self):
        """ Checks if object is beyond y bounds.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        if self.top > constants.SCREEN_HEIGHT - 1:
            return True
        if self.bottom < 0:
            return False

    def get_hit_points(self):
        """ Returns the current hit_points.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        return self.hit_points

    def add_hit_points(self, amount):
        """ Adds an amount to current hit_points.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        self.hit_points += amount

    def subtract_hit_points(self, amount):
        """ Subtracts an amount from current hit_points.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        self.hit_points -= amount

    def _rectify_angle(self):
        """ Checks to make sure angle is between 0 inclusive and 360 exclusive
            and alters angle if needed.
            
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        if self.angle == 360:
            self.angle = 0
        if self.angle < 0:
            self.angle = 360 + self.angle

    def _check_angle(self):
        """ Checks if current angle has reached target angle and
            updates change_angle and if needed.

            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        if self.target_angle == self.angle :
            self.target_angle = None #BUG probably target angle doesn't need to change
            self.change_angle = 0

    def _check_change_x(self):
        """ Checks if x velocity has reached target and
            returns True if x vel == target.
            
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        #if target x is zero, check to make sure 0 was not skipped
        if self.target_change_x == 0:
            if self.acceleration_x > 0 and self.change_x > 0:
                self.change_x = 0
            elif self.acceleration_x < 0 and self.change_x < 0:
                self.change_x = 0
        #
        if self.target_change_x == self.change_x :
            return True
        else :
            return False

    def _check_change_y(self):
        """ Checks if y velocity has reached target.
            returns True if x vel == target.
            
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        #if target y is zero, check to make sure 0 was not skiped
        if self.target_change_y == 0:
            if self.acceleration_y > 0 and self.change_y > 0:
                self.change_y = 0
            elif self.acceleration_y < 0 and self.change_y < 0:
                self.change_y = 0
        if self.target_change_y == self.change_y :
            return True
        else :
            return False

    def _check_velocity_bounds(self):
        """ Check if velocity is out of bounds (greater than max)
            set velocity to max if it is out of bounds.
            
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        if abs(self.change_x) > abs(constants.MOVEMENT_SPEED):
            if self.change_x > 0:
                self.change_x = constants.MOVEMENT_SPEED
            else :
                self.change_x = -constants.MOVEMENT_SPEED

        if abs(self.change_y) > abs(constants.MOVEMENT_SPEED):
            if self.change_y > 0:
                self.change_y = constants.MOVEMENT_SPEED
            else :
                self.change_y = -constants.MOVEMENT_SPEED
        pass

    def _accelerate_x(self):
        """ Add accel x to change x.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        self.change_x += self.acceleration_x
    
    def _accelerate_y(self):
        """ Add accel y to change y.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        self.change_y += self.acceleration_y
