def main():
    print('Example 1: for loop')
    for i in range(4):
        print(i)
    else:
        print('Completed iterating.')

    print('\nExample 2: for loop with break')
    for i in range(4):
        if i == 2:
            break
        print(i)
    else:
        print('Completed iterating.')

    print('\nExample 3: while loop')
    i = 0
    while i <= 4:
            print(i)
            i += 1
    else:
        print('Completed iterating.')

    print('\nExample 4: while loop with break')
    i = 0
    while i <= 4:
            if i == 2:
                break
            print(i)
            i += 1
    else:
        print('Completed iterating.')

main()