import random
from time import sleep

def jiggle():
    x=0
    y=0
    while True:
        x_change = random.randint(-1,1)
        y_change = random.randint(-1,1)
        x += x_change
        y += y_change
        yield (x,y)

for i in jiggle():
    print(i)
    sleep(.2)