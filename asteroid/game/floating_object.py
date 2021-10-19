import arcade
from game import constants

class FloatingObject(arcade.Sprite):
    """ An object on the screen. May or may not move.
    
        Stereotypes:
            Information Holder
        
        Attributes:
   
    """


    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)
        """ The class contructor.
        
            Args:
                self (FloatingObject): An instance of FloatingObject.
        """
        self.hit_points = None
        self.damage = None

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