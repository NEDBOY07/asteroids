from microbit import *
import music
from asteroids_model import Game

DIS_x = 5
DIS_y = 5
PLAYER_BRIGHTNESS = 9
ASTEROID_BRIGHTNESS = 5
SHOW_SCORE_SLEEP = 3000
DEAD_IMAGE = Image.ANGRY
DIED_MUSIC = music.FUNERAL
SLEEP = 20
game = Game(DIS_x, DIS_y)

while True:
    if not game.is_player_colliding():
        # model
        game.spawn_asteroids()
        game.update_asteroids()
        if button_a.get_presses():
            game.player.update(True)
        if button_b.get_presses():
            game.player.update(False)

        #view
        # display asteroid
        for asteroid in game.asteroids:
            display.set_pixel(asteroid.x, asteroid.y, ASTEROID_BRIGHTNESS)

        # display player
        display.set_pixel(game.player.x, game.player.y, PLAYER_BRIGHTNESS)

        sleep(SLEEP)
        display.clear()
        

    else: # game over display
        display.show(round((game.current_time - game.round_starting_time) / 10000))
        sleep(SHOW_SCORE_SLEEP)
        display.show(DEAD_IMAGE)
        music.play(DIED_MUSIC, wait = False, loop = True)
        # check for pin_logo
        while True:
            if pin_logo.is_touched():
                break
            
        #set variables to default
        round_starting_time = game.current_time.ticks_ms()
        alive = True
        last_spawn = game.current_time.ticks_ms()
        asteroids = []

        
    

