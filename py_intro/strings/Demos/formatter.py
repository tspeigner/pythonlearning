import math

def formatit():
    f = input("Format to try: ")
    n = eval(input("Number to format: "))
    print("Result: ", f.format(n))

    again = input("Again? Press ENTER to try another format or 'q' to quit. ")
    if again != "q":
        formatit()
   
formatit()