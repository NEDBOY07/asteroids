from microbit import *
import music
from asteroids_model.py import Game

DIS_x = 5
DIS_y = 5
PLAYER_BRIGHTNESS = 9
ASTEROID_BRIGHTNESS = 5

game = Game(DIS_x, DIS_y)

while not game.player_is_colliding():
    # model
    game.get_time_in_ms()
    game.spawn_asteroids()
    game.update_asteroids()
    game.player.update()

    #view
    # display asteroid
    for asteroid in game.asteroids:
        display.set_pixel(asteroid.x, asteroid.y, ASTEROID_BRIGHTNESS)
    display.set_pixel
    # display player
    display.set_pixel(game.player.x, game.player.y, PLAYER_BRIGHTNESS)
    

