

class GameScript:
    """ Handles the timing of events in for the game.
    
        Stereotypes:
            Information Holder
            
        Attributes:
            TODO
    """

    def __init__(self):
        """ The class constructor.
        
            Args:
                self (GameScript): An instance of GameScript.
        """
        self._score
        self._time_elapsed

        #asteroids
        self._num_basic_asteroid
        self._num_track_asteroid
        self._num_asteroid_per_second

        #enemies
        self._num_basic_enemy
        self._num_enemy_per_second

    def on_update(self):
        """ Handles what happens every frame.
        
            Args:
                self (GameScript): An instance of GameScript.
        """