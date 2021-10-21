import pytest
import sys
from pathlib import Path
import os
from asteroid.game.spawn import spawn_asteroid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from game.asteroid import Asteroid
from game.player_ship import PlayerShip
from game.spawn import SpawnPlayer
from game.spawn import SpawnAsteroid
import game.constants

import arcade


arcade.Sprite

#this first test checks that the player can always avoid a hypothetical least ideal spawned asteroid.
#this test will adapt to any arbitrary window size.
#this test is frame-based, not delta time based (how the game is currently coded)
MOVE_DELAY = .2 * 60 #human reaction time in frames.


def get_time_to_impact(pos_ship, pos_asteroid): #time/frames to impact
    velocity = 5 #from spawn_asteriod TODO make that a constant, spawn asteroid
    distance_x = pos_ship[0] - pos_asteroid[0]
    distance_y = pos_ship[1] - pos_asteroid[1]
    #TODO only works right now for horizontal or vertical amounts.
    if abs(distance_x) > 0 :
        time = distance_x / 5 #asteroid velocity max
    elif abs(distance_y) > 0 :
        time = distance_y / 5 #asteroid velocity max
    else :
        time = 0
    return abs(time) #in frames

def get_collision_radius():
    spawn = SpawnAsteroid()
    asteroid = spawn.spawn()
    radius = asteroid.collision_radius
    return radius

def worst_position(pos_ship): #generate closest possible asteroid position to ship
    width = game.constants.SCREEN_WIDTH
    height = game.constants.SCREEN_HEIGHT
    if height > width :
        pos_x = height / 2
        pos_y = pos_ship[1]
    else :
        pos_y = width / 2
        pos_x = pos_ship[0]
    return (pos_x, pos_y)

def get_ship_position():
    spawn = SpawnPlayer()
    ship = spawn.spawn()
    return (ship.center_x, ship.center_y)

def ship_avoid_distance(time): #how far can the ship run!
    speed_max = game.constants.MOVEMENT_SPEED
    assert(time - MOVE_DELAY > 0) #else test is invalid
    avoid_distance = speed_max * (time - MOVE_DELAY)
    #In reality, there should be some calculus here. generous move delay implemented instead.
    print(avoid_distance)
    return avoid_distance

#can the player always avoid taking damage from the first set of spawned asteroids?
def test_spawn_fairness():

    position_ship = get_ship_position()
    position_asteroid = worst_position(position_ship)
    time = get_time_to_impact(position_ship, position_asteroid)
    assert(ship_avoid_distance(time) > get_collision_radius())