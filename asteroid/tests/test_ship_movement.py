import pytest
import sys
from pathlib import Path
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from game.keyboard_control import KeyboardControl
from game.player_ship import PlayerShip
from game import constants
import arcade

#TEST ACCEL ON RELEASE X
#params as 1 or neg 1 for paramiterization clarity
@pytest.mark.parametrize(
    "change_x, acceleration_x, key, expected",
    [(1, 1, arcade.key.RIGHT, -1), 
    (1, -1, arcade.key.LEFT, -1),
    (-1, -1, arcade.key.LEFT, 1),
    (-1, 1, arcade.key.RIGHT, 1)]
)
def test_change_acceleration_on_release_x(change_x, acceleration_x, key, expected):
    """Test if player requested changes in acceleration behave as expected on key release.
    The player's target velocity should be set to zero on release.
    The players acceleration should be set such that change_x approaches zero."""
    expected *= constants.PLAYER_ACCELERATION #adjust to accel max.
    acceleration_x *= constants.PLAYER_ACCELERATION
    test_ship = PlayerShip()
    control = KeyboardControl()
    test_ship.change_x = change_x
    test_ship.acceleration_x = acceleration_x
    control.key_release(key, test_ship)
    assert(test_ship.acceleration_x == expected)


#TEST ACCEL ON RELEASE Y
#params as 1 or neg 1 for paramiterization clarity
@pytest.mark.parametrize(
    "change_y, acceleration_y, key, eypected",
    [(1, 1, arcade.key.UP, -1), 
    (1, -1, arcade.key.DOWN, -1),
    (-1, -1, arcade.key.DOWN, 1),
    (-1, 1, arcade.key.UP, 1)]
)
def test_change_acceleration_on_release_y(change_y, acceleration_y, key, eypected):
    """Test if player requested changes in acceleration behave as eypected on key release.
    The player's target velocity should be set to zero on release.
    The players acceleration should be set such that change_y approaches zero."""
    eypected *= constants.PLAYER_ACCELERATION #adjust to accel may.
    acceleration_y *= constants.PLAYER_ACCELERATION
    test_ship = PlayerShip()
    control = KeyboardControl()
    test_ship.change_y = change_y
    test_ship.acceleration_y = acceleration_y
    control.key_release(key, test_ship)
    assert(test_ship.acceleration_y == eypected)


#TEST ROTATION DIRECTION ON PRESS
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
    (270, 180, -1),
    (333, 270, -1),
    (333, 180, 1),
    (111, 180, 1),
    (100, 90, -1),
    (200, 180, -1),
    (200, 270, 1),
    (50, 90, 1),
    (50, 0, -1)]
)
def test_rotation_direction(angle, target, expected):
    """this test checks the direciton the ship rotates when a rotation is requested.
    The player ship should rotate clockwise/counterclockwise depending on which gets to target anagle soonest"""
    test_ship = PlayerShip()
    test_ship.angle = angle
    test_ship.target_angle = target
    control = KeyboardControl()
    assert control._rotation_direction(test_ship) == expected