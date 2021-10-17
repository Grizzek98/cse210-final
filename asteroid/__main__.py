import arcade
from game import constants
from game.director import Director

def main():
    """ The starting point of the application.

        Args:
            None
    """
    director = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    director.setup()
    arcade.run()

if __name__ == "__main__":
    main()