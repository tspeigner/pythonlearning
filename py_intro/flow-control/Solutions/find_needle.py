import random

def is_sharp(x):
    if x=='needle' or x=='Albert Einstein':
        return True
    else:
        return False

def create_haystack():
    haystack = []
    haystack.append('needle')
    for i in range(100):
        haystack.append('piece of hay')
    return haystack

def search_for_needle(haystack, n=5):
    searches = []
    for i in range(n):
        searches.append(random.choice(haystack))
    return searches

def search(searches):
    for x in searches:
        if is_sharp(x):
            print("Found needle!") #Albert wouldn't be in a haystack
            break
    else:
        print("No luck! Searching for a needle in a haystack?")

def main():
    haystack = create_haystack()
    searches = search_for_needle(haystack)
    search(searches)
    if input('Try again: (y/n) ').lower() == 'y':
        main()
    else:
        print('Goodbye!')

main()