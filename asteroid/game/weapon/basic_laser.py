from game.weapon import WeaponBase

class BasicLaser(WeaponBase):
    """ A basic burst laser weapon.

        Stereotypes:
            Information Holder

        Attributes:
            TODO
    """

    def shot(self):
        """ Instantiates an instance of BasicLaser.
        
            Args:
                self (BasicLaser): An instance of BasicLaser.
        """
        self.projectile_sprite = Projectile(path.join(constants.RESOURCE_DIRECTORY, path.join("PNG", "projectile.png")), constants.SPRITE_SCALING)
        self.projectile_sprite.center_x = self.player_ship_sprite.center_x
        self.projectile_sprite.center_y = self.player_ship_sprite.center_y - 100
