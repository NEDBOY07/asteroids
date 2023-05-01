# Imports go at the top
from microbit import *
from random import *
import time
import music


# Music
music.play(music.ENTERTAINER, wait = False, loop = True)

#CONSTANTES
ASTEROID_SPEED_MS = 100
DISPLAY_X = 5
DISPLAY_Y = 5
LIGHT_PLAYER = 9
LIGHT_ASTEROID = 5
SLEEP_TIME = 10

#VARIABLES
player_pos = 2
asteroid_pos_x = randint(0,4)
asteroid_pos_y = 0
last_update = 0
current_time = 0

# Code in a 'while True:' loop repeats forever
while True:
    # get current time
    current_time = time.ticks_ms()

    # update asteroids
    if current_time - last_update > ASTEROID_SPEED_MS:
            asteroid_pos_y += 1
            last_update = current_time
    if asteroid_pos_y == DISPLAY_Y:
            asteroid_pos_x = randint(0,DISPLAY_X - 1)
            asteroid_pos_y = 0

    # update player
    if button_a.get_presses() and player_pos > 0:
        player_pos -= 1
    if button_b.get_presses() and player_pos < DISPLAY_X - 1:
        player_pos += 1


    # collision check
    if asteroid_pos_x == player_pos and asteroid_pos_y == DISPLAY_Y - 1:
        break
        
    # display update
    display.set_pixel(asteroid_pos_x,asteroid_pos_y, LIGHT_ASTEROID)   
    display.set_pixel(player_pos,DISPLAY_Y - 1, LIGHT_PLAYER)

    #sleep
    sleep(SLEEP_TIME)
    
    display.clear()
display.show(Image.ANGRY)

music.play(music.FUNERAL, wait = False, loop = True)
