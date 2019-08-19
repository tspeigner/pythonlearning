def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '", phrase, "'", sep="")
    pos = int(input("Which character would you like to see? [Enter number] "))-1
    print("Character number ", pos+1, " is '",phrase[pos], "'",sep="")

main()