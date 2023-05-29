# ALL IMPORT STATEMENTS
import sys
import time
from random import *
 
def get_time_in_ms():# gets systemtime
    if sys.platform == 'microbit':
        return time.ticks_ms()
    return time.time()*1000
 
class Player:
    def __init__(self, _x, _y):#defines player
        self.x = _x
        self.y = _y

    def update(self, left):#updates the player
        if left:
            self.x -= 1
        else:
            self.x += 1
 
class Asteroid:
    def __init__(self,_x,_y,_speed,_l_u): #defines asteroid
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.l_u = _l_u
        self.dead = False

    def update(self):# updatesthe asteroid
        if self.current_time - self.l_u > self.speed:
            if self.y < self.DIS - 1:
                self.y += 1
                self.l_u = self.current_time
 
class Game:
    def __init__(self, _dis_x, _dis_y): # pass game settings as parameters
        self.DIS_X = _dis_x
        self.DIS_Y = _dis_y
        self.player = Player(int(self.DIS_x / 2)) # create player and attache to Game-class as attribute
        self.asteroids = [] # also create empty list for asteroids
        self.current_time = get_time_in_ms()
        self.round_starting_time = self.current_time
        self.POSSIBLE_SPAWN_RATE = 500
        self.SPAWNRARETY = 100
        self.ASTEROID_MIN_SPEED = 100
        self.ASTEROID_MAX_SPEED = 300
        self.last_spawn = 0
 
    def spawn_asteroids(self):
        #spawn
        if Game.current_time - last_spawn >= self.POSSIBLE_SPAWN_RATE and self.randint(0,100) < self.SPAWN_RARETY:
            asteroid = Asteroid(randint(0,self.DIS_X-1), 0, randint(self.ASTEROID_MIN_SPEED, self.ASTEROID_MAX_SPEED), self.current_time)
            self.asteroids.append(asteroid)
            self.last_spawn = self.current_time
 
    def update_asteroids(self):
        for asteroid in self.asteroids:
            if asteroid.y == self.DIS_Y -1:
                self.asteroids.remove(asteroid)
            asteroid.update()
            
 
    def is_player_colliding(self):
        for asteroid in self.asteroids:
            if asteroid.x == self.player.x and asteroid.y == self.DIS_Y - 1:
                return True
        return False
    