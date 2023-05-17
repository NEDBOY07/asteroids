# Imports go at the top
from microbit import *
from random import *
import time
import music

#CONSTANTES
ASTEROID_MAX_SPEED = 400
ASTEROID_MIN_SPEED = 200
DISPLAY_X = 5
DISPLAY_Y = 5
LIGHT_PLAYER = 9
LIGHT_ASTEROID = 5
SLEEP_TIME = 10
GAME_MUSIC = music.ENTERTAINER
DIED_MUSIC = music.FUNERAL
SHOW_SCORE_SPLEEP= 3000
POSSIBLE_SPAWN_RATE = 500 # in ms
SPAWN_RARETY = 10 #in percent

#VARIABLES
first_player_pos = round(DISPLAY_X/2)
current_time = 0
alive = True
round_starting_time = current_time
last_spawn = current_time
#list with all asteroids in it
asteroids = []


# Defines the class Player
class Player():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    def display(self):
        display.set_pixel(self.x, self.y, LIGHT_PLAYER)

    def update(self):#checks for pressed buttons and updates
        if button_a.get_presses() and self.x > 0:
            self.x -= 1
        if button_b.get_presses() and self.x < DISPLAY_X - 1:
            self.x += 1
        

# Defines the class Asteroid
class Asteroid():
    def __init__(self,_x,_y,_speed,_l_u):
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.l_u = _l_u
        self.dead = False
    # updates the asteroid and respwans him
    def update(self):
        if current_time - self.l_u > self.speed:
            if self.y < DISPLAY_Y - 1:
                self.y += 1
                self.l_u = current_time
            else: # spawning the asteroid at the top
                self.x = randint(0, DISPLAY_X - 1)
                self.y = 0
                self.speed = randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
                self.l_u = current_time
    def display(self):
        display.set_pixel(self.x, self.y, LIGHT_ASTEROID)
# spawnes a player
player = Player(first_player_pos, DISPLAY_Y - 1)

# Music
music.play(GAME_MUSIC, wait = False, loop = True)

# Code in a 'while True:' loop repeats forever
while True:
    if alive:
        # get current time
        current_time = time.ticks_ms()

        #spawn
        if current_time - last_spawn >= POSSIBLE_SPAWN_RATE and randint(0,100) < SPAWN_RARETY:
            asteroid = Asteroid(randint(0,DISPLAY_X-1), 0, randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED), current_time)
            asteroids.append(asteroid)
            last_spawn = current_time

        # update asteroids
        for asteroid in asteroids:
            asteroid.update()

        # update player
        player.update()

        #collision check
        for asteroid in asteroids:
            if asteroid.x == player.x and asteroid.y == DISPLAY_Y - 1:
                    alive = False
            
        # display update
        for asteroid in asteroids:
            asteroid.display()
        player.display()

        #sleep
        sleep(SLEEP_TIME)
        
        display.clear()
        
    else: # if dead
        # show score
        display.show(round((current_time - round_starting_time) / 10000))
        sleep(SHOW_SCORE_SPLEEP)
        display.show(Image.ANGRY)
        music.play(DIED_MUSIC, wait = False, loop = True)
        # check for pin_logo
        while True:
            if pin_logo.is_touched():
                break
            
        #set variables to default
        round_starting_time = time.ticks_ms()
        alive = True
        last_spawn = time.ticks_ms()
        asteroids = []