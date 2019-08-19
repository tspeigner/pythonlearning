def add_nums(num1,num2,num3=0,num4=0,num5=0):
    sum = num1 + num2 + num3 + num4 + num5
    return sum

def main():
    sum = add_nums(1,2)
    print(sum)
    sum = add_nums(sum,3)
    print(sum)
    sum = add_nums(sum,4)
    print(sum)
    sum = add_nums(sum,5)
    print(sum)
    sum = add_nums(sum,6)
    print(sum)

main()