import random
from game.floating_object import FloatingObject
from game import constants

class PowerUp(FloatingObject):
    """Handles random power ups.
    
    """
    def __init__(self, filename=None, scale=None):
        super().__init__(filename=filename, scale=scale)
        """Class constructor

            Args:
            self(PowerUp): An instance of PowerUp
        
        """
        self.power_up_list = ["shot_speed"]
        self.power_up_timer = 15

    def on_update(self, delta_time):
        """constantly checks if another power up should be created
        
        """
        pass
    
    def shot_speed_power(self):
        boosted_fire_rate = 0.5
        return boosted_fire_rate
    
    def timer_reset(self):
        self.power_up_timer = 15
    

    
