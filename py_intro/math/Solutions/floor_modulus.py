def divide(num,den):
    remainder = num % den
    floor = num // den
    print(num, 'divided by', den, 'equals',
          floor,'with a remander of', remainder)

def main():
    numerator = 5
    denominator = 2
    divide(numerator,denominator)

main()