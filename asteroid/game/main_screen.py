import arcade
from os import path
from game import constants
from game.director import Director


class MainScreen(arcade.View):

    
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Space Conquest", self.window.width / 2, self.window.height / 2,
                         arcade.color.GOLDEN_YELLOW, font_size=50, anchor_x="center")
        arcade.draw_text("Play", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.LIGHT_BLUE, font_size=20, anchor_x="center")
        arcade.draw_text("Press 'ESC' to EXIT", self.window.width / 2, self.window.height / 5 * 1,
                         arcade.color.DARK_RED, font_size=10, anchor_x="center")
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)