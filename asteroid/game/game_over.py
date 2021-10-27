import arcade
from os import path
from game.keyboard_control import KeyboardControl
from game import constants
from game.score import Score


class GameOver(arcade.View):
    """"""
    def __init__(self, score):
        super().__init__()
        self.keyboard_control = KeyboardControl()
        self.texture = arcade.load_texture(constants.SPACE_BG)
        self.score = Score()
        self.highscore = self.score.get_highscore()
        self.current_score = score
    
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("GAME OVER X-X", self.window.width / 2, self.window.height / 5 * 3,
                         arcade.color.GOLDEN_YELLOW, font_size=50, anchor_x="center")
        arcade.draw_text(f"Your Score: {self.current_score}", self.window.width / 2, self.window.height / 2-100,
                        arcade.color.LIGHT_BLUE, font_size=15, anchor_x="center")
        
        arcade.draw_text(f"BEST SCORE: {self.highscore}", self.window.width / 2, self.window.height / 5,
                         arcade.color.LIGHT_BLUE, font_size=20, anchor_x="center")
        
        
        arcade.draw_text("Press 'ESC' to EXIT", self.window.width / 2, self.window.height / 8,
                         arcade.color.DARK_RED, font_size=10, anchor_x="center")

    
    def on_key_press(self, key, modifier):
        self.keyboard_control.key_press(key)