# ALL IMPORT STATEMENTS
import sys
import time
from random import *
 
def get_time_in_ms():# gets systemtime
    if sys.platform == 'microbit':
        return time.ticks_ms()
    return time.time()*1000
 
class Player:
    def __init__(self, _x, _y, _dis_x):#defines player
        self.x = _x
        self.y = _y
        self.dis_x = _dis_x

    def update(self, left):#updates the player
        if left and self.x > 0:
            self.x -= 1
        elif not left and self.x < self.dis_x - 1:
            self.x += 1
 
class Asteroid:
    def __init__(self,_x,_y,_speed,_l_u): #defines asteroid
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.l_u = _l_u
        self.dead = False

    def update(self):# updatesthe asteroid
        if get_time_in_ms() - self.l_u > self.speed:
            self.y += 1
            self.l_u = get_time_in_ms()
 
class Game:
    def __init__(self, _dis_x, _dis_y): # pass game settings as parameters
        #Const
        self.DIS_X = _dis_x
        self.DIS_Y = _dis_y
        self.POSSIBLE_SPAWN_RATE = 200
        self.SPAWN_RARETY = 20 * self.DIS_X
        self.ASTEROID_MIN_SPEED = 200
        self.ASTEROID_MAX_SPEED = 400
        
        # variables
        self.current_time = get_time_in_ms()
        self.round_starting_time = self.current_time
        self.last_spawn = 0
        alive = True
        
        # player and asteroids
        self.player = Player(int(self.DIS_X / 2), self.DIS_Y - 1, self.DIS_X) # create player and attache to Game-class as attribute
        self.asteroids = [] # create empty list for asteroids
        
 
    def spawn_asteroids(self):
        #spawn
        if get_time_in_ms() - self.last_spawn >= self.POSSIBLE_SPAWN_RATE and randint(0,100) < self.SPAWN_RARETY:
            asteroid = Asteroid(randint(0,self.DIS_X-1), 0, randint(self.ASTEROID_MIN_SPEED, self.ASTEROID_MAX_SPEED),self.current_time)
            self.asteroids.append(asteroid)
            self.last_spawn = get_time_in_ms()
 
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

    def get_time(self):
        time = get_time_in_ms()
        return time