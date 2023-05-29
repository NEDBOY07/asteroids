from microbit import *
import music
from asteroids_model.py import Game

DIS_x = 5
DIS_y = 5
PLAYER_BRIGHTNESS = 9
ASTEROID_BRIGHTNESS = 5
SHOW_SCORE_SLEEP = 3000
DEAD_IMAGE = Image.ANGRY

game = Game(DIS_x, DIS_y)

while True:
    if not game.player_is_colliding():
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
    else:
        display.show(round((game.current_time - game.round_starting_time) / 10000))
        sleep(SHOW_SCORE_SPLEEP)
        display.show(DEAD_IMAGE)
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
    

