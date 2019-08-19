def main():
    num=0
    print('Loop 1:')
    while num < 6:
        print(num)
        num += 1

    print('\nLoop 2:')
    for num in range(6):
        print(num)

    print('\nLoop 3:')
    for num in range(0,6):
        print(num)

    print('\nLoop 4:')
    for num in range(1,11,2):
        print(num)

    print('\nLoop 5:')
    for num in range(10,0,-1):
        print(num)

    print('\nLoop 6:')
    nums = [0,1,2,3,4,5] #list
    for num in nums:
        print(num)

    print('\nLoop 7:')
    nums = (0,1,2,3,4,5) #tuple
    for num in nums:
        print(num)

    grades = {'English':97, 'Math':93, 'Art':74, 'Music':86}
    
    print('\nLoop 8:')
    for course in grades:
        print(course)

    print('\nLoop 9:')
    for course in grades.keys():
        print(course)

    print('\nLoop 10:')
    for grade in grades.values():
        print(grade)

    print('\nLoop 11:')
    for num in range(6):
        print(num)
        if num > 3:
            break

    print('\nLoop 12:')
    for num in range(6):
        if num==3:
            continue
        print(num)

main()