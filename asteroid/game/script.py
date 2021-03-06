import game.constants
from game import enemy

class GameScript():
    """Controls the state of the game based on time since start and score
    Game script is largely a table. For a given time, it will return
    a certain required game state.
    override for different level patterns.
        Stereotypes: Data holder

        attributes:
            total_time (float), time since the game began
            enemy_spawn_rate (float), enemy spawns per second
            enemy_max (int), maximum number of enemies on screen
    """
    #could implement a time/score table for more interesting level complete REQs
    #But levels and a such a table are outside the scope of this project.
    def __init__(self) -> None:
        """the class constructor"""
        self.total_time = 0
        self.enemy_spawn_rate = 1 #Smallest needed interum between spawns

        #time_separations
        #implemented this way for customizability.
        self.time_category = 0
        self.time_0 = 0
        self.time_1 = 7
        self.time_2 = 15
        self.time_3 = 25
        self.time_4 = 37
        self.time_5 = 42
        self.allowed_enemies = [[enemy.Asteroid, 30]] #pointer to object of allowed spawns
                                                #a list of lists, each list containing
                                                #the object name and current num_allowed.

    def _update_time_category(self):
        """get current time catagory based on time
        args:
            self: an instance of GameScript"""
        if self.total_time < self.time_1 :
            self.time_category = 0
        elif self.total_time < self.time_2 :
            self.time_category = 1
        elif self.total_time < self.time_3 :
            self.time_category = 2
        elif self.total_time < self.time_4 :
            self.time_category = 3
        elif self.total_time < self.time_5 :
            self.time_category = 4
        elif self.total_time > self.time_5 :
            self.time_category = 5

    def update_game_state(self):
        """update spawn rate based on time category
        args:
            self: an instance of GameScript"""
        if self.time_category == 0 :
            self.enemy_spawn_rate = .4

        elif self.time_category == 1 :

            self.enemy_spawn_rate = .2
        elif self.time_category == 2 :

            self.enemy_spawn_rate = .1

        elif self.time_category == 3 :
            self.enemy_spawn_rate = .05

        elif self.time_category == 4 :
            self.enemy_spawn_rate = .02

        elif self.time_category == 5 :
            self.enemy_spawn_rate = .01


    def update(self, delta_time):
        """The update method to be called every frame."""
        self.total_time += delta_time
        self._update_time_category()
        self.update_game_state()
        
    #debug methods
    def set_time(self,time):
        """set a time to check a given state"""
        self.total_time = time