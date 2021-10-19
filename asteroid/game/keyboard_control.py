
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
    def _rotation_direction(self, ship):
        """determines the direction of rotation that gets to target angle quickest
        Returns 1 for clockwise, -1 for counterclockwise"""
        angle = ship.angle
        target = ship.target_angle
        if target == 0: 
            target = 360 #assumes circle from 0 exclusive - 360 inlcusive

        #special cases. counter_clockwise and clockwise are equivelent these cases.
        if angle == 180 and target == 90 :
            return -1
        if angle == 270 and target == 180:
            return -1 
        counter_clockwise = target #return 1
        clockwise = target - 360 #return -1
        if abs(angle - counter_clockwise) > abs(angle - clockwise):
            return -1
        else :
            return 1

        #relationship between positive and negative
    # def _rotation_direction(self, ship):
    #     """returns clockwise (1) counterclockwise (-1) depending on which is most expeditious

    #         Args:
    #             ship (PlayerShip): a controllabe ship
    #     """
    #     if (ship.angle > 180) and (ship.target_angle == 0): 
    #         ship.target_angle = 360
    #     if ship.angle <= ship.target_angle :
    #         return 1
    #     else :
    #         return -1

    def key_press(self, key, ship, modifier=None):
        """ On key press controls
        
            Args: 
                self (KeyboardControl): An instance of KeyboardControl.
                key (int): The key being pressed (uses arcade table).
                ship (PlayerShip): a controllable ship
                modifier (int): Any modifiers pressed with key.
        """
        if control_dict.get(key, None) is not None:
            ship.target_angle = control_dict.get(key)

            ship.change_angle = constants.PLAYER_ROTATION_SPEED * self._rotation_direction(ship)

        if key == arcade.key.LEFT:
            ship.target_change_x = -constants.MOVEMENT_SPEED
            ship.acceleration_x = -constants.PLAYER_ACCELERATION
        if key == arcade.key.RIGHT:
            ship.target_change_x = constants.MOVEMENT_SPEED
            ship.acceleration_x =  constants.PLAYER_ACCELERATION
        if key == arcade.key.UP:
            ship.target_change_y = constants.MOVEMENT_SPEED
            ship.acceleration_y =  constants.PLAYER_ACCELERATION
        if key == arcade.key.DOWN:
            ship.target_change_y = -constants.MOVEMENT_SPEED
            ship.acceleration_y = -constants.PLAYER_ACCELERATION
        if key == arcade.key.SPACE:
            #TODO in a bullet hell, typically you can shoot and move in different directions
            #using arrow keys for movement and WASD for firing direction
            #though having some time to rotation sounds pretty good. Probably a short time.
            #Let's keep this for now and see how it feels, but we may want to make auto-shoot on
            #any WASD
            ship.is_shooting = True

    def key_release(self, key, ship, modifier=None):
        """ On key release controls
        
            Args: 
                self: An instance of KeyControl.
                key (int): The key being pressed (uses arcade table).
                ship (PlayerShip): a controllable ship
                modifier (int): Any modifiers pressed with key.
        """

        #if a key is released and the ship is going the direction
        #the key represents, reverse acceleration direcion.
        #and set target_change to zero
        print(key, arcade.key.LEFT)
        print(ship.acceleration_x)
        if key == arcade.key.LEFT and ship.acceleration_x < 0 :
            ship.acceleration_x *= -1
            ship.target_change_x = 0
        if key == arcade.key.RIGHT and ship.acceleration_x > 0 :
            ship.acceleration_x *= -1
            ship.target_change_x = 0
        if key == arcade.key.DOWN and ship.acceleration_y < 0 :
            ship.acceleration_y *= -1
            ship.target_change_y = 0
        if key == arcade.key.UP and ship.acceleration_y > 0 :
            ship.acceleration_y *= -1
            ship.target_change_y = 0

        # if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        #     ship.change_x = 0
        # if key == arcade.key.UP or key == arcade.key.DOWN:
        #     ship.change_y = 0

        #TODO in a bullet hell, typically you can shoot and move in different directions
        #using arrow keys for movement and WASD for firing direction
        #though having some time to rotation sounds pretty good. Probably a short time.
        #Let's keep this for now and see how it feels, but we may want to make auto-shoot on
        #any WASD
        if key == arcade.key.SPACE:
            ship.is_shooting = False
            pass