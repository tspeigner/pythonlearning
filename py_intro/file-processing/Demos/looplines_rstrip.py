with open('my_files/zen_of_python.txt') as f:
    for line in f:
        print( line.rstrip() )