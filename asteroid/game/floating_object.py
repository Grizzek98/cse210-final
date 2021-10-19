import arcade
from game import constants

class FloatingObject(arcade.Sprite):
    """ An object on the screen. May or may not move.
    
        Stereotypes:
            Information Holder
        
        Attributes:
   
    """
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture = None, angle: float = 0, hit_points = 100, damage = 100):
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle)

    # def __init__(self, filename, scale):
    #     super().__init__(filename=filename, scale=scale)
        """ The class contructor.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
                all sprite params
                hit_points (int) starting HP
                damage (int) damage dealt on contact
        """
        self.hit_points = hit_points
        self.damage = damage

    def update(self):
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
        """Rotates the object according to self.change_angle
            Assumes degrees"""
        self.angle += self.change_angle
        pass
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