import sys

def main(args):    
    with open(args[1]) as f1:
        list_1 = f1.read().splitlines()

    with open(args[2]) as f2:
        list_2 = f2.read().splitlines()

    list_1_only = []
    list_2_only = []
    
    for item in list_1:
        if item not in list_2:
            list_1_only.append(item)
    
    for item in list_2:
        if item not in list_1:
            list_2_only.append(item)

    print('List 1 Only: ', str(list_1_only))
    print('List 2 Only: ', str(list_2_only))

if __name__ == '__main__':
    main(sys.argv)