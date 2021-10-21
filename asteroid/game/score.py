from game import constants

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
        self._high_score = self.get_stored_highscore()
        self.score_file = constants.HIGHSCORE_FILE

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

    def write_highscore(self, score_file, highscore):
        """Saves the High Score to the txt file

            Args:
            self(Score): An instance of Score
            score_file(string): The path of the file that tracks the high score
            highscore(int): The score to be stored

        """
        with(open(score_file,'w')) as file:
            file.write(str(highscore))

    def set_highscore(self):
        self._high_score = self.get_stored_highscore()
    
    def get_highscore(self):
        """Gets the current value in highscore
        
            Args:
            self(Score): An instance of Score
            
        """
        return self._high_score

    def check_highscore(self, current_score, current_high):
        """Checks if the current score surpasses the current highscore

            Args:
            self(Score): An instance of Score
            score_file(string): The address of the file that tracks the high score 
        """
        if current_score > current_high:
            return True
        else: 
            return False

    def get_stored_highscore(self):
        """Gets the current stored highscore
        
            Args:
            self(Score): An instance of Score          
        """
        #Opens the file with stored data
        try: #If the file is not created yet (Fist time playing) it won't break
            with(open(constants.HIGHSCORE_FILE,'r')) as file:
                highscore = file.read()
            #Checks if it is not empty
                if type(highscore) is not None and highscore != '':
                    highscore = int(highscore)
                else:
                    highscore = 0
        except:
            with(open(constants.HIGHSCORE_FILE,'w')) as file:
                file.write("0")
                highscore = 0
            
        return highscore

    def update_highscore(self):
        
        stored_score = self.get_stored_highscore()
        current_score = self.get_score()

        if self.check_highscore(current_score, stored_score):
            self.write_highscore(constants.HIGHSCORE_FILE, current_score)
            self.set_highscore()

    


