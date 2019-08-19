def running_sum(total=0):
    try:
        num = int(input('Enter a number: '))
    except ValueError:
        print('Integers only please. Try again.')
    else:
        total += num
        print('The current total is:', total)
        
    running_sum(total)

def main():
    running_sum()

main()