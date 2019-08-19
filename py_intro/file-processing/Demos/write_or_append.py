def write(mode):
    with open('my_files/notes.txt', mode) as f:
        f.seek(0)
        print('File Contents when opened:\n' + f.read())
        while True:
            note = input('Add a note (Q to quit): ')
            if note.upper() == 'Q':
                break
            f.write(note + '\n')

        f.seek(0)    
        print('File Contents before closing:\n' + f.read())

def main():
    mode = ''
    while mode not in ['w','a']:
        mode = input('Enter "w" to write or "a" to append: ')
    if mode == 'w':
        write('w+')
    else:
        write('a+')
        
main()