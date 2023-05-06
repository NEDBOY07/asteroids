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

#VARIABLES
player_pos = round(DISPLAY_X/2)
current_time = 0
alive = True
round_starting_time = 0

# Defines the class Asteroid
class Asteroid():
    def __init__(self,_x,_y,_speed,_l_u):
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.l_u = _l_u
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

#ASTEROIDS
a_1 = Asteroid(randint(0, DISPLAY_X-1), 0, randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED), 0)
a_2 = Asteroid(randint(0, DISPLAY_X-1), 0, randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED), 0)
a_3 = Asteroid(randint(0, DISPLAY_X-1), 0, randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED), 0)
a_4 = Asteroid(randint(0, DISPLAY_X-1), 0, randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED), 0)
# puts all astroids in a list
asteroids = [a_1, a_2, a_3, a_4]

# Music
music.play(GAME_MUSIC, wait = False, loop = True)

# Code in a 'while True:' loop repeats forever
while True:
    if alive:
        # get current time
        current_time = time.ticks_ms()

        # update asteroids
        for asteroid in asteroids:
            asteroid.update()

        # update player
        if button_a.get_presses() and player_pos > 0:
            player_pos -= 1
        if button_b.get_presses() and player_pos < DISPLAY_X - 1:
            player_pos += 1

        #collision check
        for asteroid in asteroids:
            if asteroid.x == player_pos and asteroid.y == DISPLAY_Y - 1:
                alive = False
            
        # display update
        for asteroid in asteroids: #checks for each astroid's position
            display.set_pixel(asteroid.x, asteroid.y, LIGHT_ASTEROID)
        display.set_pixel(player_pos,DISPLAY_Y - 1, LIGHT_PLAYER)

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
        player_pos = 2
        current_time = 0
        alive = True
        round_starting_time = current_time

        

        
