from random import randint

def roll_dice():
    return (randint(1,6), randint(1,6), randint(1,6))

def play():
    n=0
    while True:
        n+=1
        r = roll_dice()
        print('{}: {},{},{}'.format(n, r[0], r[1], r[2]))
        if r[0] == r[1] == r[2]:
            print('Wow! Triples!')
        input()

def main():
    input('Press ENTER to roll the dice. ')
    play()

main()