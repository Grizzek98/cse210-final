import arcade
from os import path
from game.keyboard_control import KeyboardControl
from game import constants
from game.director import Director


class InstructionsScreen(arcade.View):
    """The How-to-play screen to be shown before the game starts
    
    """
    def __init__(self):
        super().__init__()
        self.keyboard_control = KeyboardControl()
        self.texture = arcade.load_texture(constants.INSTRUCIONS_BG)

    
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)   
    
    def on_key_press(self, key, modifier):
        self.keyboard_control.key_press(key)