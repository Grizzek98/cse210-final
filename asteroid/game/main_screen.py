import arcade
from os import path
from game.keyboard_control import KeyboardControl
from game import constants
from game.director import Director
from game.score import Score


class MainScreen(arcade.View):
    """"""
    def __init__(self):
        super().__init__()
        self.keyboard_control = KeyboardControl()
        self.texture = arcade.load_texture(constants.MAIN_MENU_BG)
        self.sound_song = arcade.load_sound(constants.BG_MUSIC)
        self.score = Score()
        self.highscore = self.score.get_highscore()
    
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)
        arcade.play_sound(self.sound_song)
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text(f"BEST SCORE: {self.highscore}", self.window.width / 2, self.window.height / 5,
                         arcade.color.GOLDEN_YELLOW, font_size=15, anchor_x="center")
        arcade.draw_text("Play", self.window.width / 2, self.window.height / 2-100,
                         arcade.color.LIGHT_BLUE, font_size=50, anchor_x="center")
        arcade.draw_text("Press 'ESC' to EXIT", self.window.width / 2, self.window.height / 8,
                         arcade.color.DARK_RED, font_size=10, anchor_x="center")

        
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_key_press(self, key, modifier):
        self.keyboard_control.key_press(key)