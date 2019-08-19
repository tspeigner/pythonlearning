def running_sum(total=0):
    num = input('Enter a number: ')
    
    if not num.isdigit():
        print('Integers only please. Try again.')
    else:
        total += int(num)
        print('The current total is:', total)
        
    running_sum(total)

def main():
    running_sum()

main()