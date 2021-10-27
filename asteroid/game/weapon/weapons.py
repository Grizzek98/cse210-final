from arcade import Sprite
from game.weapon.projectile import Projectile

class Weapons():
    """ The fundamental class of a weapon object. Other weapon classes inherit from this one.

        Stereotypes:
            Information Holder, service provider

        Attributes:
            fire_rate (float) minimum time between shots
            _current_fire_interval (float) time since last shot
            projectile_sprite (Projectile)
    """

    def __init__(self) -> None:
        """ The class constructor.
        
            Args:
                self (Weapon): An instance of Weapon.
        """
        self.fire_rate = .3
        self._current_fire_interval = 0 #time since last fire
        self.projectile = Projectile
        self.weapon_damage = 10
        self.weapon_piercing = 0 

    def can_fire(self, rate_modifier: float = 1) -> bool:
        """Return true if weapon can fire
            args:
                self (Weapon) an instance of weapon
                rate_modifier (float) any multiplicative power up modifiers to fire rate. """
        return self._current_fire_interval >= self.fire_rate * rate_modifier

    def generate_shot(self, ship: Sprite, damage_modifier: float = 1) -> Projectile: #pew pew
        """Returns a projectile with correct positon and orientation
            args: 
                ship (Sprite) the object 'creating' the shot
                rate_modifier (float_ any multiplicative power up mod to damage"""
        damage = self.weapon_damage * damage_modifier
        self._current_fire_interval = 0
        return self.projectile(center_x= ship.center_x, center_y = ship.center_y, angle= ship.angle, damage= damage, num_pierce= self.weapon_piercing)

    def on_update(self, delta_time: float) -> None:
        """update fire interval for time
            args: delta_time (float) time since last frame"""
        self._current_fire_interval += delta_time


