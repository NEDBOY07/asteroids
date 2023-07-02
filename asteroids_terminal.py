from asteroids_model import Game
import os
import time

N_X = 80  # Change the size as desired
N_Y = 8  # Change the size as desired
game = Game(N_X, N_Y)

while True:    
    for y in range(N_Y):
        s = ""
        for x in range(N_X):
            asteroid_found = False
            for asteroid in game.asteroids:
                if asteroid.x == x and asteroid.y == y:
                    s += "*"
                    asteroid_found = True
                    break
            if not asteroid_found:
                s += " "
        print(s)
    os.system('cls' if os.name == 'nt' else 'clear')
    # model
    game.update_asteroids()
    game.spawn_asteroids()