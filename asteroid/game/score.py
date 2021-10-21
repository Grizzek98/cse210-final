

class Score:
    """ This is where score related stuff lives.
    
        Stereotypes:
            Information Holder
        
        Attributes:
            _score (int): A score that increases as asteroids and enemies are destroyed
            _high_score (int): The highest score acheived to date. Stored in a file, 
                and retreived from hence.
    """

    def __init__(self):
        """ The class contructor.
        
            Args:
                self (Score): An instance of Score.
        """
        self._score = 0
        self._high_score = None

    def get_score(self):
        """ Returns the current score.
        
            Args:
                self (Score): An instance of Score.
        """
        return self._score

    def add_score(self, amount):
        """ Adds an amount to the current score.
        
            Args:
                self (Score): An instance of Score.
        """
        self._score += amount
        #print("Score: ", self.get_score())

    def subtract_score(self, amount):
        """ Subtracts an amount from the current score.
        
            Args:
                self (Score): An instance of Score.
        """
        self._score -= amount