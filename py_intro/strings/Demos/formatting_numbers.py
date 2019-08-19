import math
import random

print('pi equals {:f}'.format(math.pi))
print('negative pi equals {:f}'.format(-math.pi))

#Always show sign
print('pi equals {:+f}'.format(math.pi))
print('negative pi equals {:+f}'.format(-math.pi))

#Let's not be so precise
print('pi equals {:+.2f}'.format(math.pi))

#Let's be really precise
print('pi equals {:.20f}'.format(math.pi))

#Alignment
print("\nALIGNMENT (Defaults to Right Alignment for Numbers")
for i in range(1,10):
    num = random.randint(-200,200) + random.random()
    print('{:10.2f}'.format(num))

##Left Align
print("\nLEFT ALIGNMENT")
for i in range(1,10):
    num = random.randint(-200,200) + random.random()
    print('{:<10.2f}'.format(num))

##Center
print("\nCENTER ALIGNMENT")
for i in range(1,10):
    num = random.randint(-200,200) + random.random()
    print('{:^10.2f}'.format(num))

##Change fill
print("\nCENTER ALIGNMENT WITH FILL")
for i in range(1,10):
    num = random.randint(-200,200) + random.random()
    print('{:.^10.2f}'.format(num))

#Percentage Format
print("\nPERCENTAGE")
for i in range(1,10):
    num = random.random()
    print('{:8.2%}'.format(num))

##Separate the Thousands
print("\nTHOUSANDS")
for i in range(1,10):
    num = random.randint(-10000000,10000000) + random.random()
    print('{:15,.2f}'.format(num))