
import arcade
from game import constants
control_dict = { #dict belongs outside so it doesn't have to get constructed every call
    arcade.key.W: constants.SPRITE_UP,
    arcade.key.A: constants.SPRITE_LEFT,
    arcade.key.S: constants.SPRITE_DOWN,
    arcade.key.D: constants.SPRITE_RIGHT,
}
#     arcade.key.UP: "up",
#     arcade.key.LEFT: "left",
#     arcade.key.DOWN: "down",
#     arcade.key.RIGHT: "right"
# }
class KeyboardControl():
    """ Contains the methods for controlling objects needing keyboard control

        Stereotypes:
            Information Holder

        Attributes: 
            None
    """
    def key_press(self, key, sprite, modifier=None):
        """ On key press controls
        
            Args: 
                self (KeyboardControl): An instance of KeyboardControl.
                key (int): The key being pressed (uses arcade table).
                sprite (Sprite): An arcade sprite.
                modifier (int): Any modifiers pressed with key.
        """
        if control_dict.get(key, None) is not None:
            sprite.angle = control_dict.get(key)
            #TODO shot code
        if key == arcade.key.LEFT:
            sprite.change_x = -constants.MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            sprite.change_x =  constants.MOVEMENT_SPEED
        if key == arcade.key.UP:
            sprite.change_y =  constants.MOVEMENT_SPEED
        if key == arcade.key.DOWN:
            sprite.change_y = -constants.MOVEMENT_SPEED
            
        if key == arcade.key.SPACE:
            #TODO in a bullet hell, typically you can shoot and move in different directions
            #using arrow keys for movement and WASD for firing direction
            #though having some time to rotation sounds pretty good. Probably a short time.
            #Let's keep this for now and see how it feels, but we may want to make auto-shoot on
            #any WASD
            sprite.is_shooting = True


    def key_release(self, key, sprite, modifier=None):
        """ On key release controls
        
            Args: 
                self: An instance of KeyControl.
                key (int): The key being pressed (uses arcade table).
                sprite (Sprite): An arcade sprite.
                modifier (int): Any modifiers pressed with key.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            sprite.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            sprite.change_y = 0
        #TODO shot code

        #TODO in a bullet hell, typically you can shoot and move in different directions
        #using arrow keys for movement and WASD for firing direction
        #though having some time to rotation sounds pretty good. Probably a short time.
        #Let's keep this for now and see how it feels, but we may want to make auto-shoot on
        #any WASD
        if key == arcade.key.SPACE:
            sprite.is_shooting = False
            pass