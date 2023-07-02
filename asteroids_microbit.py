from microbit import *
import music
from asteroids_model import Game

DIS_x = 5
DIS_y = 5
PLAYER_BRIGHTNESS = 9
ASTEROID_BRIGHTNESS = 5
DEAD_IMAGE = Image.ANGRY
DIED_MUSIC = music.FUNERAL
SLEEP = 20
game = Game(DIS_x, DIS_y)
alive = True

while True:
    if alive:
        # model
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

        if game.is_player_colliding():
            alive = False

        sleep(SLEEP)
        display.clear()
        
    else: # game over display
        survived_time = round((game.get_time() - game.round_starting_time)/1000)
        display.scroll(survived_time)
        display.show(DEAD_IMAGE)
        music.play(DIED_MUSIC, wait = False, loop = True)
        # check for pin_logo
        while True:
            if pin_logo.is_touched():#set variables to default
                break
        game.round_starting_time = game.get_time()
        last_spawn = game.get_time()
        asteroids = []
        alive = True
