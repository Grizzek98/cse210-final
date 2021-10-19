import pytest
import sys
from pathlib import Path
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from game.keyboard_control import KeyboardControl
from game.player_ship import PlayerShip
from game import constants


#Can't use fixtures to reuturn initialzed object. Very sad.
@pytest.mark.parametrize(
    "angle, target, expected",
    [(90, 0, -1),
    (270, 0, 1),
    (133, 270, 1),
    (180, 90, -1),
    (30, 270, -1),
    (300, 90, 1),
    (0, 90, 1),
    (0, 270, -1),
    (270, 180, -1)]
)
def test_rotation_direction(angle, target, expected):
    test_ship = PlayerShip()
    test_ship.angle = angle
    test_ship.target_angle = target
    control = KeyboardControl()
    assert control._rotation_direction(test_ship) == expected