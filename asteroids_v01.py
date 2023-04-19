from microbit import *
from random import *
s = "00000:00000:00000:00000:00900"
pos_p = 3
pos_a = 0
asteroid = False
while True:
    img = Image(s)
    display.show(img)
    if button_a.get_presses():
        pos_p -= 1
    if button_b.get_presses():
        pos_p += 1

    if asteroid == False:
        asteroid = True
        pos_a = randint(1,5)

    else:
        pass
    if pos_a == 1:
        s = "50000:00000:00000:00000:00000"
    elif pos_a == 2:
        s = "05000:00000:00000:00000:00000"
    elif pos_a == 3:
        s = "00500:00000:00000:00000:00000"
    elif pos_a == 4:
        s = "00050:00000:00000:00000:00000"
    elif pos_a == 5:
        s = "00005:00000:00000:00000:00000"
    img = Image(s)
    display.show(img)
    
    if pos_p == 1:
        s = "00000:00000:00000:00000:90000"
    elif pos_p == 2:
        s = "00000:00000:00000:00000:09000"
    elif pos_p == 3:
        s = "00000:00000:00000:00000:00900"
    elif pos_p == 4:
        s = "00000:00000:00000:00000:00090"
    elif pos_p == 5:
        s = "00000:00000:00000:00000:00009"




        
        
        