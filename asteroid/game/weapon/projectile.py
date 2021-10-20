import arcade

class Projectile(arcade.Sprite):
    """ The base file for the actual sprite created when a weapon is fired.
    
        Stereotypes:
            Information Holder
            
        Attributes:
            TODO
    """

    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture = None, angle: float = 0,
    damage = 10, does_pierce = False, num_pierce = 0):
        super().__init__(filename=filename, scale=scale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle)
        """ The class constructor.
        
            Args:
                self (PewpewVisual): An instance of PewpewVisual.
        """
        self._damage = damage
        self._does_pierce = does_pierce
        self._num_pierce = num_pierce