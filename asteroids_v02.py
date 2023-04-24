# Imports go at the top
from microbit import *
from random import *
import time

player_pos = 2
asteroid = False
asteroid_pos_x = randint(0,4)
asteroid_pos_y = 0
last_update = 0

# Code in a 'while True:' loop repeats forever
while True:
    display.set_pixel(player_pos,4,9)
    
    if button_a.get_presses() and player_pos > 0:
        player_pos -= 1
    if button_b.get_presses() and player_pos < 4:
        player_pos += 1

    if asteroid == False:
        asteroid_pos_x = randint(0,4)
        asteroid_pos_y = 0
        asteroid = True
        print("asteroid = False")

    if asteroid == True:
        if time.ticks_ms()- last_update > 500:
            asteroid_pos_y += 1
        display.set_pixel(asteroid_pos_x,asteroid_pos_y,9)
        last_update = time.ticks_ms()
        if asteroid_pos_y == 4:
            asteroid = False

    if asteroid_pos_x == player_pos and asteroid_pos_y == 4:
        break

    sleep(50)
    display.clear()
display.show(Image.ANGRY)
