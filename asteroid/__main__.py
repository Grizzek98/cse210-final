import arcade
from game import constants
from game.director import Director
from game.main_screen import MainScreen

def main():
    """ The starting point of the application.

        Args:
            None
    """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = MainScreen()
    game_view = Director()
    window.show_view(start_view)
    game_view.setup()
    arcade.run()

if __name__ == "__main__":
    main()