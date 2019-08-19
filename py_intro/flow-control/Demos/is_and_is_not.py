def main():
    a = [1,2,3,4]
    b = [1,2,3,4]
    c = a
    print('a == b:', a == b)
    print('a is b:', a is b)
    print('a == c:', a == c)
    print('a is c:', a is c)

    a.append(5)
    print(c)

main()