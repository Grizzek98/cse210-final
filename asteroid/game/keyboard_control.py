
import arcade
from game import constants

class KeyboardControl:
    """ Handles keyboard input given by the user.
    
        Stereotypes:
            Service Provider
        
        Attributes:
            NONE
    """

    def key_press(self, key):
        """ Handles key press logic.

            Args:
                self (KeyboardControl): An instance of KeyboardControl.
        """
        if key == arcade.key.LEFT:
            self.change_x = -constants.MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.change_x = constants.MOVEMENT_SPEED
        if key == arcade.key.UP:
            self.change_y = constants.MOVEMENT_SPEED
        if key == arcade.key.DOWN:
            self.change_y = -constants.MOVEMENT_SPEED

    def key_release(self, key):
        """ Handles key release logic

            Args:
                self (KeyboardControl): An instance of KeyboardControl.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.change_y = 0