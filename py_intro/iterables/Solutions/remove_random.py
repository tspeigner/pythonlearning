import random

def remove_random(l):
    x = random.choice(l)
    l.remove(x)
    return x

def main():
    colors = ['red','blue','green','orange']
    removed_color = remove_random(colors)
    print('The removed color was', removed_color)
    print('The remaining colors are', colors)

main()