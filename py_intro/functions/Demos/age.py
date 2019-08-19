import greetings

def main():
    first_name = input("What's your name? ")
    age = input(greetings.formal(first_name) + " How old are you? ")
    print("Wow!", first_name, "You look great for " + age + "!")
    guessed_age = int(age) - 10
    print("I would have guessed you were only", str(guessed_age) + ".")

main()