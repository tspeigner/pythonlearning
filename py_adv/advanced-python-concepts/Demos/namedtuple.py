from collections import namedtuple

Point = namedtuple('point','x, y')

# set target position:
target_pos = Point(100,200)

# get x value of target position
print(target_pos.x)