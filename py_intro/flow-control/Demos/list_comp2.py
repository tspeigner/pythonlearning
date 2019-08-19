def initials(name):
    fullname = name.split(' ')
    initials = (fullname[0][0],fullname[1][0])
    return initials

def main():
    names = ['Graham Chapman', 'John Cleese', 'Eric Idle',
             'Terry Gilliam', 'Terry Jones', 'Michael Palin']
    inits = [initials(name) for name in names]
    for i in inits:
        print(i[0] + '.' + i[1] + '.')
    
main()