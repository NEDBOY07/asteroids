from asteroids_model import Game
import os


N_COLLUMS = 100
N_ROWS = 10

game = Game(N_COLLUMS, N_ROWS)

while True:
    os.system('cls')
    for y in range(N_ROWS):
        s = ""
        for x in range(N_COLLUMS):
            ast = False
            for asteroid in game.asteroids:
                if asteroid.x == x and asteroid.y == y:
                    ast = True
                    break
            if ast:
                s = s + "*"
            else:
                s = s + "."
        print(s)
    game.update_asteroids()
    game.spawn_asteroids()
        